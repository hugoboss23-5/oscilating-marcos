from marcos import Marcos

m_yin = Marcos(mode="yin")
out1 = m_yin.step({"x": 1, "y": None})
assert out1 == {"x": 1}

m_yang = Marcos(mode="yang")
out2 = m_yang.step({"x": 1, "y": None})
assert out2 == {"x": 1, "y": None}

print("OK")
