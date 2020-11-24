"""
input_=> [1, 2, 3, 4, 77, 78, 79, 88, 89, 100, 101, 102, 103, 200, 201, 202, 4321]
flat_list_=> [1, 1, 1, 73, 1, 1, 9, 1, 11, 1, 1, 1, 97, 1, 1, 4119]
cut_locations_=> [3, 6, 8, 12, 15]
====================
[[1, 2, 3, 4]]
[[1, 2, 3, 4], [77, 78, 79]]
[[1, 2, 3, 4], [77, 78, 79], [88, 89]]
[[1, 2, 3, 4], [77, 78, 79], [88, 89], [100, 101, 102, 103]]
[[1, 2, 3, 4], [77, 78, 79], [88, 89], [100, 101, 102, 103], [200, 201, 202]]
[[1, 2, 3, 4], [77, 78, 79], [88, 89], [100, 101, 102, 103], [200, 201, 202], [4321]]
====================
loot_=> [[1, 2, 3, 4], [77, 78, 79], [88, 89], [100, 101, 102, 103], [200, 201, 202], [4321]]
"""



def flatten_gap(list):
    '''
    flattens list making sequential numbers into 1
    '''
    list.sort()
    gap = []
    while (len(list) > 1):
        first = list.pop(0)
        second = list[0]
        gap.append(abs(second - first))
    return gap

def get_cut_position(flat_list):
    '''
    returns a list containing where to cut positions should be.
    if number!= 1 cut here
    '''
    return [i for i, x in enumerate(flat_list) if x != 1]


def cut_list(list,cut_positions):
    '''
    [1, 2, 3, 4, 77, 78, 79, 88, 89, 100, 101, 102, 103, 200, 2001, 2002] # list start with
    [3, 6, 8, 12, 13] # cut list at these spots
    cuts # cut start
    cute # cut end
    '''
    print '=='*10
    new_list = []
    cuts = 0

    for cute in cut_positions:
        new_list.append(list[cuts:cute+1])
        cuts = cute+1

        print new_list

    new_list.append(list[cuts:])
    print new_list
    print '==' * 10
    return new_list

points = [1,2,3,4,77,78,79,88,89,100,101,102,103,200,201,202,4321]
tmp = tuple(points)

flat_list = flatten_gap(points)
cut_positions = get_cut_position(flat_list)

points = list(tmp)
print 'input_=>',points
print 'flat_list_=>',flat_list
print 'cut_locations_=>',cut_positions

loot = cut_list(points,cut_positions)
print 'loot_=>',loot
