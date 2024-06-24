import pyglet
from pyglet.gl import *
import numpy as np
from pyrr import Matrix44, Vector3

# Importar funciones de OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Dimensiones del cubo
CUBE_SIZE = 3

# Definir los vértices y colores del cubo
vertices = [
    # Cara frontal
    -1, -1,  1,
     1, -1,  1,
     1,  1,  1,
    -1,  1,  1,
    # Cara trasera
    -1, -1, -1,
    -1,  1, -1,
     1,  1, -1,
     1, -1, -1,
    # Otras caras
    -1,  1, -1,
    -1,  1,  1,
     1,  1,  1,
     1,  1, -1,
    -1, -1, -1,
     1, -1, -1,
     1, -1,  1,
    -1, -1,  1,
    -1, -1, -1,
    -1, -1,  1,
    -1,  1,  1,
    -1,  1, -1,
     1, -1, -1,
     1,  1, -1,
     1,  1,  1,
     1, -1,  1,
]

# Definir los colores de cada vértice
colors = [
    1, 0, 0,
    1, 0, 0,
    1, 0, 0,
    1, 0, 0,
    0, 1, 0,
    0, 1, 0,
    0, 1, 0,
    0, 1, 0,
    0, 0, 1,
    0, 0, 1,
    0, 0, 1,
    0, 0, 1,
    1, 1, 0,
    1, 1, 0,
    1, 1, 0,
    1, 1, 0,
    1, 0, 1,
    1, 0, 1,
    1, 0, 1,
    1, 0, 1,
    0, 1, 1,
    0, 1, 1,
    0, 1, 1,
    0, 1, 1,
]

indices = [
    0, 1, 2,  2, 3, 0,
    4, 5, 6,  6, 7, 4,
    8, 9, 10, 10, 11, 8,
    12, 13, 14, 14, 15, 12,
    16, 17, 18, 18, 19, 16,
    20, 21, 22, 22, 23, 20,
]

vertices_gl = (GLfloat * len(vertices))(*vertices)
colors_gl = (GLfloat * len(colors))(*colors)
indices_gl = (GLuint * len(indices))(*indices)

class RubiksCubeWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=800, height=600, caption='Rubik\'s Cube 3D', resizable=True)
        self.rotation = Vector3([0.0, 0.0, 0.0])
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        self.set_minimum_size(400, 300)
        self.init_gl()

    def init_gl(self):
        glEnable(GL_DEPTH_TEST)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices_gl)
        glColorPointer(3, GL_FLOAT, 0, colors_gl)

    def on_draw(self):
        self.clear()
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(self.rotation.x, 1.0, 0.0, 0.0)
        glRotatef(self.rotation.y, 0.0, 1.0, 0.0)
        glRotatef(self.rotation.z, 0.0, 0.0, 1.0)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices_gl)

    def update(self, dt):
        self.rotation.y += 30.0 * dt
        if self.rotation.y > 360:
            self.rotation.y -= 360

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, width / float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

if __name__ == '__main__':
    window = RubiksCubeWindow()
    pyglet.app.run()
