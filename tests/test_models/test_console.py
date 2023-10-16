import unittest
from unittest.mock import patch
from io import StringIO
import os

from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    @patch('sys.stdout', new_callable=StringIO)
    def capture_stdout(self, command, mock_stdout):
        with patch('builtins.input', return_value=command):
            self.console.cmdloop()
        return mock_stdout.getvalue().strip()

    def test_quit_command(self):
        output = self.capture_stdout("quit")
        self.assertEqual(output, "")

    def test_EOF_command(self):
        output = self.capture_stdout("EOF")
        self.assertEqual(output, "")

    def test_create_command(self):
        output = self.capture_stdout("create BaseModel")
        self.assertTrue(len(output) == 36)  # Expecting UUID

    def test_show_command(self):
        create_output = self.capture_stdout("create BaseModel")
        id_str = create_output.split()[-1]
        show_output = self.capture_stdout(f"show BaseModel {id_str}")
        self.assertIn("BaseModel", show_output)

    def test_destroy_command(self):
        create_output = self.capture_stdout("create BaseModel")
        id_str = create_output.split()[-1]
        destroy_output = self.capture_stdout(f"destroy BaseModel {id_str}")
        show_output = self.capture_stdout(f"show BaseModel {id_str}")
        self.assertIn("** no instance found **", show_output)

    def test_all_command(self):
        create_output = self.capture_stdout("create BaseModel")
        all_output = self.capture_stdout("all BaseModel")
        self.assertIn("BaseModel", all_output)

    def test_count_command(self):
        create_output = self.capture_stdout("create BaseModel")
        count_output = self.capture_stdout("count BaseModel")
        self.assertEqual(count_output, "1")

    def test_update_command(self):
        create_output = self.capture_stdout("create BaseModel")
        id_str = create_output.split()[-1]
        update_output = self.capture_stdout(f"update BaseModel {id_str} name 'New Name'")
        show_output = self.capture_stdout(f"show BaseModel {id_str}")
        self.assertIn("New Name", show_output)

    def test_update_dict_command(self):
        create_output = self.capture_stdout("create BaseModel")
        id_str = create_output.split()[-1]
        update_output = self.capture_stdout(f"update_dict BaseModel {id_str} {{'name': 'New Name'}}")
        show_output = self.capture_stdout(f"show BaseModel {id_str}")
        self.assertIn("New Name", show_output)

if __name__ == '__main__':
    unittest.main()
