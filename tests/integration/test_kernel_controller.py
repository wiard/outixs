import unittest
from kernel.core.kernel_controller import KernelController

class TestKernelController(unittest.TestCase):
    
    def setUp(self):
        self.controller = KernelController()
    
    def tearDown(self):
        pass

    def test_kernel_start(self):
        result = self.controller.start()
        self.assertEqual(result, "Kernel started successfully")
    
    def test_kernel_stop(self):
        result = self.controller.stop()
        self.assertEqual(result, "Kernel stopped successfully")
    
    def test_kernel_config(self):
        result = self.controller.get_config()
        self.assertIsInstance(result, dict)
        self.assertIn('config_key', result)
        self.assertEqual(result['config_key'], 'value')
    
    def test_invalid_operation(self):
        with self.assertRaises(AttributeError):
            self.controller.invalid_method()

if __name__ == '__main__':
    unittest.main()

