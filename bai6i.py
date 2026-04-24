# i) Kiểm tra 3 cạnh tam giác và loại tam giác
def check_triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Không phải tam giác"
    
    # Kiểm tra tính chất
    is_can = (a == b or b == c or a == c)
    is_deu = (a == b == c)
    # Kiểm tra Pitago cho tam giác vuông 
    sides = sorted([a, b, c])
    is_vuong = math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

    if is_deu: return "Tam giác đều"
    if is_vuong and is_can: return "Tam giác vuông cân"
    if is_vuong: return "Tam giác vuông"
    if is_can: return "Tam giác cân"
    return "Tam giác thường"

triangle_info = lambda a, b, c: check_triangle_type(a, b, c)
