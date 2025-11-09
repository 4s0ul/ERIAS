# entry
md1, mnd1 = 0.8, 0.3
md2, mnd2 = 0.75, 0.25
md3, mnd3 = 0.4, 0.5
md4, mnd4 = 0.85, 0.2

# e1 (and)
md_e1 = min(md1, md2)
mnd_e1 = max(mnd1, mnd2)
ku_e1 = md_e1 - mnd_e1

# e2 (or)
md_e2 = max(md3, md4)
mnd_e2 = min(mnd3, mnd4)
ku_e2 = md_e2 - mnd_e2

# combination
md_combined = md_e1 + md_e2 * (1 - md_e1)
mnd_combined = mnd_e1 + mnd_e2 * (1 - mnd_e1)
ku_combined = md_combined - mnd_combined

print('e1:\n', 'md', md_e1, '| mdn:', mnd_e1, '| ku: ', ku_e1)
print('e2:\n', 'md:', md_e2, '| md:', mnd_e2, '| ku:', ku_e2)
print('combination:\n', 'md:', md_combined, '| mnd:', mnd_combined, '| md:', ku_combined)
