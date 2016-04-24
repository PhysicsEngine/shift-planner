#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Shift(Object):
	@classmethod:
	build(cls, member_num, days, pattern_num):
		 return pulp.LpVariable.dicts('shift', (member_num, days, pattern_num), 0, 1, 'Binary')
  
