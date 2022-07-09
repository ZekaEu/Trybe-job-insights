from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('src/jobs.csv', 'python') == 1639
    assert count_ocurrences('src/jobs.csv', 'PyThOn') == 1639
    assert count_ocurrences('src/jobs.csv', 'JAVASCRIPT') == 122
    assert count_ocurrences('src/jobs.csv', 'jAvAsCrIpT') == 122
