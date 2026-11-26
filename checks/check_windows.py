"""Offline arithmetic checks for the fictional tool-library cases."""
from fractions import Fraction
import copy
import json
from pathlib import Path
import unittest

DATA=Path(__file__).resolve().parents[1]/'data'/'windows.json'


def ceiling(row):
    fields=('confirmed','prepared','passed','eligible_opening','authorize','pickup')
    if any(type(row[k]) is not int or row[k]<0 for k in fields):
        raise ValueError('counts must be nonnegative integers')
    if row['passed']>row['prepared']:
        raise ValueError('new passed supply exceeds new prepared stock')
    return min(row['confirmed'],row['passed']+row['eligible_opening'],row['authorize'],row['pickup'])


def filled(row):
    if not 0 <= row['handed_off'] <= row['confirmed'] or row['confirmed']==0:
        raise ValueError('invalid numerator or denominator')
    return Fraction(row['handed_off'],row['confirmed'])


class WindowsTest(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(DATA.read_text())
        self.c={r['label']:r for r in self.data['scenarios']}

    def test_authorized_baseline_and_regression(self):
        a,b=self.data['observed']
        self.assertEqual(a['prepared'], b['prepared'])
        self.assertEqual((filled(a),filled(b)),(Fraction(5,6),Fraction(7,12)))
        self.assertEqual(filled(a)-filled(b),Fraction(1,4))
        self.assertEqual((ceiling(self.c['baseline']),ceiling(self.c['changed'])),(20,14))

    def test_extra_prep_not_increasing_ceiling(self):
        a,b=self.c['changed'],self.c['prep_push']
        self.assertEqual((ceiling(a),ceiling(b)),(14,14))
        self.assertEqual((a['prepared']-a['passed'],b['prepared']-b['passed']),(4,10))
        self.assertEqual(b['passed']-b['authorize'],6)

    def test_staff_and_inspection(self):
        self.assertEqual(ceiling(self.c['extra_signer']),18)
        self.assertEqual(ceiling(self.c['failed_batch']),12)

    def test_opening_stock_and_counter_capacity(self):
        self.assertEqual(ceiling(self.c['carryover']),16)
        no_stock=copy.deepcopy(self.c['carryover'])
        no_stock['eligible_opening']=0
        self.assertEqual(ceiling(no_stock),12)
        self.assertEqual(ceiling(self.c['counter_loss']),9)
        self.assertEqual(ceiling({**self.c['counter_loss'],'authorize':18}),9)

    def test_invalid_stock_cannot_be_counted(self):
        with self.assertRaises(ValueError):
            ceiling({**self.c['changed'],'passed':25})
        with self.assertRaises(ValueError):
            ceiling({**self.c['changed'],'eligible_opening':-1})

    def test_denominator_is_not_invented(self):
        with self.assertRaises(ValueError):
            filled({'confirmed':0,'handed_off':0})
        with self.assertRaises(ValueError):
            filled({'confirmed':14,'handed_off':20})


if __name__=='__main__':
    unittest.main(verbosity=2)
