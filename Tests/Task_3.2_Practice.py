# def test_input_text(expected_result, actual_result):
#    assert expected_result == actual_result, "Expected " + str(expected_result) + ", got " + str(actual_result)
#
# # test_input_text(8, 11)
# test_input_text(11, 11)
# test_input_text(11, 15)

# s = 'My Name is Julia'
#
# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')

def test_substring(full_string, substring):
   assert substring in full_string , "expected '" + str(substring) + "' to be substring of '" + str(full_string) + "'"

test_substring('fulltext', 'some_text')

