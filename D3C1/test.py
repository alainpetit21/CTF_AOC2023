import main


def test_loading():
    data = main.load_data("example2.txt")
    main.data = data

    # Should work v
    assert (data[0][0] == '*')
    assert (data[9][2] == '6')

    # Should fail v
    # assert (data[9][0] == '6')


def test_symbol_scanner():
    gen_function = main.symbols_scanner()

    assert (next(gen_function) == (0, 0))
    assert (next(gen_function) == (9, 0))
    assert (next(gen_function) == (3, 1))
    assert (next(gen_function) == (6, 3))
    assert (next(gen_function) == (3, 4))
    assert (next(gen_function) == (5, 5))
    assert (next(gen_function) == (3, 8))
    assert (next(gen_function) == (5, 8))
    assert (next(gen_function) == (0, 9))
    assert (next(gen_function) == (9, 9))


def test_kernel_processor():
    gen_function = main.kernel_processor(0, 1)

    assert (next(gen_function) == (1, 0))

    gen_function = main.kernel_processor(3, 1)
    assert (next(gen_function) == (2, 0))
    assert (next(gen_function) == (2, 2))
    assert (next(gen_function) == (3, 2))

    gen_function = main.kernel_processor(6, 3)
    assert (next(gen_function) == (6, 2))
    assert (next(gen_function) == (7, 2))

    gen_function = main.kernel_processor(3, 4)
    assert (next(gen_function) == (2, 4))

    gen_function = main.kernel_processor(5, 5)
    assert (next(gen_function) == (4, 6))

    gen_function = main.kernel_processor(3, 8)
    assert (next(gen_function) == (2, 9))
    assert (next(gen_function) == (3, 9))

    gen_function = main.kernel_processor(5, 8)
    assert (next(gen_function) == (6, 7))
    assert (next(gen_function) == (5, 9))
    assert (next(gen_function) == (6, 9))

    gen_function = main.kernel_processor(0, 9)
    assert (next(gen_function) == (1, 9))


def test_detect_whole_humber():
    assert (main.detect_whole_number(2, 0) == (67, (1, 0)))
    assert (main.detect_whole_number(1, 0) == (67, (1, 0)))

    assert (main.detect_whole_number(5, 0) == (114, (5, 0)))
    assert (main.detect_whole_number(6, 0) == (114, (5, 0)))
    assert (main.detect_whole_number(7, 0) == (114, (5, 0)))

    assert (main.detect_whole_number(2, 2) == (35, (2, 2)))
    assert (main.detect_whole_number(3, 2) == (35, (2, 2)))

    assert (main.detect_whole_number(6, 2) == (633, (6, 2)))
    assert (main.detect_whole_number(7, 2) == (633, (6, 2)))
    assert (main.detect_whole_number(8, 2) == (633, (6, 2)))

    assert (main.detect_whole_number(0, 4) == (617, (0, 4)))
    assert (main.detect_whole_number(1, 4) == (617, (0, 4)))
    assert (main.detect_whole_number(2, 4) == (617, (0, 4)))

    assert (main.detect_whole_number(7, 5) == (58, (7, 5)))
    assert (main.detect_whole_number(8, 5) == (58, (7, 5)))

    assert (main.detect_whole_number(2, 6) == (592, (2, 6)))
    assert (main.detect_whole_number(3, 6) == (592, (2, 6)))
    assert (main.detect_whole_number(4, 6) == (592, (2, 6)))

    assert (main.detect_whole_number(6, 7) == (755, (6, 7)))
    assert (main.detect_whole_number(7, 7) == (755, (6, 7)))
    assert (main.detect_whole_number(8, 7) == (755, (6, 7)))

    assert (main.detect_whole_number(1, 9) == (664, (1, 9)))
    assert (main.detect_whole_number(2, 9) == (664, (1, 9)))
    assert (main.detect_whole_number(3, 9) == (664, (1, 9)))

    assert (main.detect_whole_number(5, 9) == (598, (5, 9)))
    assert (main.detect_whole_number(6, 9) == (598, (5, 9)))
    assert (main.detect_whole_number(7, 9) == (598, (5, 9)))


def test_process_queue():
    main.add_number_to_processing_queue(1, 9)
    main.add_number_to_processing_queue(5, 9)

    assert (main.process_queue() == 598+664)


if __name__ == '__main__':
    test_loading()
    test_symbol_scanner()
    test_kernel_processor()
    test_detect_whole_humber()
    test_process_queue()

    print("passed all tests")

