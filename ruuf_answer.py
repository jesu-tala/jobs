def panel_bigger_than_roof(x_panel, y_panel, x_roof, y_roof):
    var_left = y_roof
    if x_panel > x_roof:
        var_left = x_roof
        if x_panel > y_roof:
            return True 
    if y_panel >  var_left:
        return True
    return False

def square_panel(x_panel, y_panel):
    return (x_panel == y_panel)
    
def find_max_amount_panels(x_panel, y_panel, x_roof, y_roof):
    x_panel,y_panel = max(x_panel,y_panel), min(x_panel,y_panel) 
    x_roof,y_roof = max(x_roof,y_roof), min(x_roof,y_roof) 
    
    if panel_bigger_than_roof(x_panel, y_panel, x_roof, y_roof):
        return 0
    if square_panel(x_panel, y_panel):
        return ((x_roof // x_panel) * (y_roof // y_panel)) #Techo 5x3 = 5 || Panel 2x2 5 // 2 = 2 , 3 // 2 = 1
        
    return ((x_roof * y_roof) // (x_panel * y_panel)) # Techo 5x3 = 15 , Panel 1x2 = 2  , 15 // 2 = 7


def test():
    assert(find_max_amount_paneles(1, 2, 3, 5) == 7)

test()
print(f"Panel 2x2 || Techo 3x5 --> 2 = {find_max_amount_paneles(2,2,3,5)}?")
print(f"Panel 1x2 || Techo 3x5 --> 7 = {find_max_amount_paneles(1,2,3,5)}?")
print(f"Panel 2x1 || Techo 3x5 --> 7 = {find_max_amount_paneles(2,1,3,5)}?")
print(f"Panel 3x3 || Techo 7x7 --> 4 = {find_max_amount_paneles(3,3,7,7)}?")
print(f"Panel 2x2 || Techo 4x4 --> 4 = {find_max_amount_paneles(2,2,4,4)}?")
print(f"Panel 1x2 || Techo 4x4 --> 8 = {find_max_amount_paneles(1,2,4,4)}?")
print(f"Panel 3x2 || Techo 4x4 --> 2 = {find_max_amount_paneles(3,2,4,4)}?")
print(f"Panel 1x2 || Techo 2x4 --> 4 = {find_max_amount_paneles(1,2,2,4)}?")
print(f"Panel 2x2 || Techo 1x10 --> 0 = {find_max_amount_paneles(2,2,1,10)}?")
print(f"Panel 3x2 || Techo 3x1 --> 0 = {find_max_amount_paneles(3,2,3,1)}?")
print(f"Panel 1x2 || Techo 10x1 --> 5 = {find_max_amount_paneles(1,2,10,1)}?")
print(f"Panel 2x2 || Techo 2x2 --> 1 = {find_max_amount_paneles(2,2,2,2)}?")
