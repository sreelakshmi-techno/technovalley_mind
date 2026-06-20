import importlib
import os
import shutil
import tempfile
import unittest
from pathlib import Path


class MemoryPersistenceTests(unittest.TestCase):

    def load_memory_modules(self, db_path):
        os.environ["TECHVALLEY_MEMORY_DB_PATH"] = str(db_path)

        import memory.local_store as local_store
        import memory.short_memory as short_memory
        import memory.long_memory as long_memory
        import memory.profile_memory as profile_memory
        import memory.memory_manager as memory_manager

        importlib.reload(local_store)
        importlib.reload(short_memory)
        importlib.reload(long_memory)
        importlib.reload(profile_memory)
        importlib.reload(memory_manager)

        return local_store, short_memory, long_memory, profile_memory, memory_manager

    def test_memory_updates_existing_turn_and_persists_profile(self):
        fd, db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        os.unlink(db_path)

        try:
            _, _, _, _, memory_manager = self.load_memory_modules(Path(db_path))

            memory_manager.save_memory("session-1", "My name is Alice", "")
            memory_manager.save_memory("session-1", "My name is Alice", "Hello Alice")

            history = memory_manager.get_memory("session-1")["short_memory"]

            self.assertEqual(len(history), 1)
            self.assertEqual(history[0]["user"], "My name is Alice")
            self.assertEqual(history[0]["assistant"], "Hello Alice")

            profile_memory = memory_manager.get_profile_memory("session-1")

            self.assertEqual(profile_memory["name"], "Alice")

        finally:
            for suffix in ["", "-wal", "-shm"]:
                candidate = Path(f"{db_path}{suffix}")
                try:
                    candidate.unlink()
                except OSError:
                    pass

    def test_memory_loads_persisted_history_after_reload(self):
        fd, db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        os.unlink(db_path)

        try:
            _, _, _, _, memory_manager = self.load_memory_modules(Path(db_path))

            memory_manager.save_memory("session-2", "I need help with admission", "Sure")

            reloaded_memory_manager = importlib.reload(importlib.import_module("memory.memory_manager"))

            history = reloaded_memory_manager.get_memory("session-2")["short_memory"]

            self.assertEqual(len(history), 1)
            self.assertEqual(history[0]["user"], "I need help with admission")
            self.assertEqual(history[0]["assistant"], "Sure")

        finally:
            for suffix in ["", "-wal", "-shm"]:
                candidate = Path(f"{db_path}{suffix}")
                try:
                    candidate.unlink()
                except OSError:
                    pass


if __name__ == "__main__":
    unittest.main()
