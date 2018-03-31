from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch


class ItemModelTestPass(models_tests.ItemModelTest):

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(ItemModelTestPass, self).setUp()

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemModelTestPass, self).tearDown()

    @rmotr_tester(PASS)
    @patch("todo.tests.test_models.Item", mocked_models.Item._get())
    def test_saving_and_retrieving_items(self):
        super(ItemModelTestPass, self).test_saving_and_retrieving_items()


class ItemModelTestFail(models_tests.ItemModelTest):

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(ItemModelTestFail, self).setUp()

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemModelTestFail, self).tearDown()

    @rmotr_tester(FAIL)
    @patch("todo.tests.test_models.Item", mocked_models.Item._get())
    def test_saving_and_retrieving_items(self):
        with patch('test_utils.mocked_models.MockIterator') as fake_iterator:
            fake_iterator.count.return_value = 0
            fake_iterator.__getitem__.return_value = mocked_models.ItemObject()
            super(ItemModelTestFail, self).test_saving_and_retrieving_items()
