from .base import FunctionalTest
import time

TEST_EMAIL = 'edith@mockmyid.com'


class MyListsTest(FunctionalTest):

	def test_logged_in_users_lists_are_saved_as_my_lists(self):
		# Edith is a logged-in user
		self.create_pre_authenticated_session('edith@example.com')
		time.sleep(3)

		# She goes to the home page and starts a list
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Chickens\n')
		self.get_item_input_box().send_keys('Ducks\n')
		first_list_url = self.browser.current_url

		# She notices a "My lists" link, for the first time
		self.browser.find_element_by_link_text('My lists').send_keys("\n")

		# She sees that her list is in there, named according to its
		# first list item
		time.sleep(3)
		self.browser.find_element_by_link_text('Chickens').send_keys("\n")
		self.wait_for(
			lambda: self.assertEqual(self.browser.current_url, first_list_url)
		)
		# She decides to start another list, just to see
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Click cows\n')
		second_list_url = self.browser.current_url

		# Under "My lists", her new list appears
		self.browser.find_element_by_link_text('My lists').send_keys("\n")
		time.sleep(3)		
		self.browser.find_element_by_link_text('Click cows').click()
		self.assertEqual(self.browser.current_url, second_list_url)

		# She logs out. The "My lists" option disappears
		self.browser.find_element_by_id('id_logout').click()
		time.sleep(3)
		self.assertEqual(
			self.browser.find_elements_by_link_text('My lists'),
			[]
		)