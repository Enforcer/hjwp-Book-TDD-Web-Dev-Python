#!/usr/bin/env python3
import unittest

from book_parser import Command, Output
from book_tester import ChapterTest


class Chapter8Test(ChapterTest):
    chapter_name = "chapter_08_prettification"
    previous_chapter = "chapter_07_working_incrementally"

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, "code listing with git ref")
        self.assertEqual(type(self.listings[1]), Command)
        self.assertEqual(type(self.listings[2]), Output)

        self.start_with_checkout()
        # other prep
        self.sourcetree.run_command("python3 manage.py migrate --noinput")
        # self.unset_PYTHONDONTWRITEBYTECODE()
        self.prep_virtualenv()
        self.sourcetree.run_command("uv pip install pip")

        # skips
        self.skip_with_check(24, "the -w means ignore whitespace")
        self.skip_with_check(27, "leave static, for now")
        self.skip_with_check(52, "will now show all the bootstrap")
        self.skip_with_check(55, "we need the 'cssselect'")

        # hack fast-forward
        self.skip_forward_if_skipto_set()

        while self.pos < len(self.listings):
            print(self.pos)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(ignore=["moves"])


if __name__ == "__main__":
    unittest.main()
