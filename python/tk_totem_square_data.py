def rectangle_coordinates_from_coordinate_pair(coordinate_pair, canvas_height):
    x = coordinate_pair[0]
    y = coordinate_pair[1]
    scale = 10
    return scale * x, \
           canvas_height - scale * y, \
           scale * x + scale, \
           canvas_height - (scale * y + scale)


def rectangle_color_from_shape(shape):
    if shape == "L":
        return 'purple'
    if shape == "J":
        return 'green'
    if shape == "I":
        return 'cyan'
    if shape == "O":
        return 'orange'
    if shape == "T":
        return 'yellow'
    if shape == "S":
        return 'red'
    if shape == "Z":
        return 'blue'


class TkTotemSquareData:
    def __init__(self, scale, canvas_height):
        self.scale = scale
        self.canvas_height = canvas_height
        self.rectangle_ids = list()

    def clear_rectangles_in_canvas(self, canvas):
        for id in self.rectangle_ids:
            canvas.delete(id)
        self.rectangle_ids.clear()

    def create_rectangles_in_canvas(self, canvas, totem_answers):
        for totem_answer in totem_answers:
            for coordinate_pair in totem_answer.coordinates:
                rectangle_coordinates = rectangle_coordinates_from_coordinate_pair(coordinate_pair, self.canvas_height)
                rectangle_color = rectangle_color_from_shape(totem_answer.shape)
                id = canvas.create_rectangle(rectangle_coordinates, fill=rectangle_color)
                self.rectangle_ids.append(id)
