from pyslab.naked_singles import find_in_rows, find_in_columns, find_in_nonets


class TestFindInRows:
    def test_known_board(self, str_to_puzzle_candidates):

        elem, num = find_in_rows(
            *str_to_puzzle_candidates(
                "403010005056480100200000040900004000005020600000700008020000006008036910600090507"
            )
        ).pop()

        assert elem == (6, 2)
        assert num == 9

    def test_one_single(self, simple_puzzle, simple_candidates):

        expected_elem = (0, 0)
        expected_value = simple_puzzle[expected_elem]
        simple_puzzle[expected_elem] = 0

        actual_elem, actual_value = find_in_rows(simple_puzzle, simple_candidates).pop()

        assert actual_elem == expected_elem
        assert actual_value == expected_value

    def test_multiple_same_row(self, simple_puzzle, simple_candidates):

        expected_elems = [(0, 0), (0, 1)]
        expected_values = [simple_puzzle[elem] for elem in expected_elems]
        for elem in expected_elems:
            simple_puzzle[elem] = 0

        singles = list(find_in_rows(simple_puzzle, simple_candidates))

        actual_elems = [elem for elem, num in singles]
        actual_values = [num for elem, num in singles]

        assert actual_elems == expected_elems
        assert actual_values == expected_values

    def test_multiple_different_row(self, simple_puzzle, simple_candidates):

        expected_elems = [(0, 0), (1, 1)]
        expected_values = [simple_puzzle[elem] for elem in expected_elems]
        for elem in expected_elems:
            simple_puzzle[elem] = 0

        singles = list(find_in_rows(simple_puzzle, simple_candidates))

        actual_elems = [elem for elem, num in singles]
        actual_values = [num for elem, num in singles]

        assert actual_elems == expected_elems
        assert actual_values == expected_values


class TestFindInColumns:
    def test_known_board(self, str_to_puzzle_candidates):

        elem, num = find_in_columns(
            *str_to_puzzle_candidates(
                "500000100008290050090007004000102009070854010100906000800700030020019800004000001"
            )
        ).pop()

        assert elem == (1, 5)
        assert num == 1

    def test_one_single(self, simple_puzzle, simple_candidates):

        expected_elem = (0, 0)
        expected_value = simple_puzzle[expected_elem]
        simple_puzzle[expected_elem] = 0

        actual_elem, actual_value = find_in_columns(
            simple_puzzle, simple_candidates
        ).pop()

        assert actual_elem == expected_elem
        assert actual_value == expected_value

    def test_multiple_same_column(self, simple_puzzle, simple_candidates):

        expected_elems = [(0, 0), (1, 0)]
        expected_values = [simple_puzzle[elem] for elem in expected_elems]
        for elem in expected_elems:
            simple_puzzle[elem] = 0

        singles = list(find_in_columns(simple_puzzle, simple_candidates))

        actual_elems = [elem for elem, num in singles]
        actual_values = [num for elem, num in singles]

        assert actual_elems == expected_elems
        assert actual_values == expected_values

    def test_multiple_different_column(self, simple_puzzle, simple_candidates):

        expected_elems = [(0, 0), (1, 1)]
        expected_values = [simple_puzzle[elem] for elem in expected_elems]
        for elem in expected_elems:
            simple_puzzle[elem] = 0

        singles = list(find_in_columns(simple_puzzle, simple_candidates))

        actual_elems = [elem for elem, num in singles]
        actual_values = [num for elem, num in singles]

        assert actual_elems == expected_elems
        assert actual_values == expected_values


class TestFindInNonets:
    def test_known_board(self, str_to_puzzle_candidates):

        elem, num = find_in_nonets(
            *str_to_puzzle_candidates(
                "605020308000000000003706009760003000001548700000600031200901400000000000104060807"
            )
        ).pop()

        assert elem == (3, 7)
        assert num == 8

    def test_one_single(self, simple_puzzle, simple_candidates):

        expected_elem = (0, 0)
        expected_value = simple_puzzle[expected_elem]
        simple_puzzle[expected_elem] = 0

        actual_elem, actual_value = find_in_nonets(
            simple_puzzle, simple_candidates
        ).pop()

        assert actual_elem == expected_elem
        assert actual_value == expected_value

    def test_multiple_same_column(self, simple_puzzle, simple_candidates):

        expected_elems = [(0, 0), (1, 0)]
        expected_values = [simple_puzzle[elem] for elem in expected_elems]
        for elem in expected_elems:
            simple_puzzle[elem] = 0

        singles = list(find_in_nonets(simple_puzzle, simple_candidates))

        actual_elems = [elem for elem, num in singles]
        actual_values = [num for elem, num in singles]

        assert actual_elems == expected_elems
        assert actual_values == expected_values

    def test_multiple_different_column(self, simple_puzzle, simple_candidates):

        expected_elems = [(0, 0), (1, 1)]
        expected_values = [simple_puzzle[elem] for elem in expected_elems]
        for elem in expected_elems:
            simple_puzzle[elem] = 0

        singles = list(find_in_nonets(simple_puzzle, simple_candidates))

        actual_elems = [elem for elem, num in singles]
        actual_values = [num for elem, num in singles]

        assert actual_elems == expected_elems
        assert actual_values == expected_values
