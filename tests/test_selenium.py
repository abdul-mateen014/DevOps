import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NotesAppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up ChromeDriver once for all tests"""
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=options)
        cls.base_url = "http://localhost"
        cls.wait = WebDriverWait(cls.driver, 10)
    
    @classmethod
    def tearDownClass(cls):
        """Close driver after all tests"""
        cls.driver.quit()
    
    def test_01_homepage_loads(self):
        """Test 1: Verify homepage loads successfully"""
        self.driver.get(self.base_url)
        self.wait.until(lambda driver: driver.title == "Semester Notes App")
        self.assertEqual(self.driver.title, "Semester Notes App")
        heading = self.driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertEqual(heading, "Notes App")
        print("✅ Test 1 PASSED: Homepage loads successfully")
    
    def test_02_form_elements_visible(self):
        """Test 2: Verify form elements are visible"""
        self.driver.get(self.base_url)
        input_field = self.wait.until(EC.presence_of_element_located((By.ID, "title")))
        self.assertTrue(input_field.is_displayed())
        add_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.assertTrue(add_button.is_displayed())
        print("✅ Test 2 PASSED: Form elements are visible")
    
    def test_03_add_note(self):
        """Test 3: Add a note and verify it appears"""
        self.driver.get(self.base_url)
        note_text = f"Test Note {int(time.time())}"
        input_field = self.wait.until(EC.presence_of_element_located((By.ID, "title")))
        input_field.clear()
        input_field.send_keys(note_text)
        add_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        add_button.click()
        time.sleep(2)
        notes_list = self.driver.find_elements(By.CSS_SELECTOR, ".notes li")
        self.assertGreater(len(notes_list), 0)
        print(f"✅ Test 3 PASSED: Note added successfully")
    
    def test_04_form_validation(self):
        """Test 4: Form validation - empty note"""
        self.driver.get(self.base_url)
        self.wait.until(EC.presence_of_element_located((By.ID, "note-form")))
        add_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        add_button.click()
        time.sleep(1)
        status = self.driver.find_element(By.ID, "status").text
        self.assertIn("Please enter a note", status)
        print("✅ Test 4 PASSED: Form validation working")
    
    def test_05_delete_note(self):
        """Test 5: Delete a note"""
        self.driver.get(self.base_url)
        # Add a note first
        note_text = f"Delete Test {int(time.time())}"
        input_field = self.wait.until(EC.presence_of_element_located((By.ID, "title")))
        input_field.clear()
        input_field.send_keys(note_text)
        add_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        add_button.click()
        time.sleep(2)
        # Now delete it
        initial_notes = self.driver.find_elements(By.CSS_SELECTOR, ".notes li")
        if len(initial_notes) > 0:
            delete_button = initial_notes[0].find_element(By.CSS_SELECTOR, "button")
            delete_button.click()
            time.sleep(2)
            updated_notes = self.driver.find_elements(By.CSS_SELECTOR, ".notes li")
            self.assertLess(len(updated_notes), len(initial_notes))
            print("✅ Test 5 PASSED: Note deleted successfully")
    
    def test_06_api_health(self):
        """Test 6: Check API health endpoint"""
        import requests
        response = requests.get("http://localhost:3000/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        print("✅ Test 6 PASSED: API health check successful")

if __name__ == "__main__":
    unittest.main(verbosity=2)
