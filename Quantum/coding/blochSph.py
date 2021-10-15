import drawSvg as draw
import latextools
from bloch_sphere.animate_bloch_compare import render_animation

# Add some extra labels
zero_ket = draw.Group()
zero_ket.draw(latextools.render_snippet('$\ket{0}$', latextools.pkg.qcircuit),
              x=0, y=0, center=True, scale=0.015)
one_ket = draw.Group()
one_ket.draw(latextools.render_snippet('$\ket{1}$', latextools.pkg.qcircuit),
             x=0, y=0, center=True, scale=0.015)
zero_ket_inner = draw.Use(zero_ket, 0, 0, transform='scale(0.75)')
one_ket_inner = draw.Use(one_ket, 0, 0, transform='scale(0.75)')

w = 624*2  # Output width
fps = 20
draw_args = dict(
    w = w/2,
    outer_labels=[
        [(0, 0, 1), (-0.15, 0.13), zero_ket],
        [(0, 0, -1), (0.15, -0.13), one_ket],
    ],
    inner_labels=[
        [(0, 0, 0.8), (0, 0), zero_ket_inner],
        [(0, 0, -0.8), (0, 0), one_ket_inner],
    ],
)

gates1 = 'h,z,h'.split(',')
gates2 = 'x'.split(',')
def func1(state):
    state.draw_args = dict(draw_args)
    state.draw_args['inner_labels'] = []
    state.sphere_fade_in()
    state.apply_gate_list(gates1, final_wait=False)
    state.wait()
    for _ in gates2:
        state.i_gate()
    state.wait()
    state.wait()
    state.sphere_fade_out()
    state.wait()
def func2(state):
    state.draw_args = dict(draw_args)
    state.draw_args['inner_labels'] = []
    state.sphere_fade_in()
    for _ in gates1:
        state.i_gate()
    state.wait()
    state.apply_gate_list(gates2, final_wait=False)
    state.wait()
    state.wait()
    state.sphere_fade_out()
    state.wait()

render_animation('hzh_x_compare', func1, func2,
                 r'& \gate{H} & \gate{Z} & \gate{H} & \qw & \push{=} & & \gate{X} & \qw',
                 r'$HZH\ket{\psi}=X\ket{\psi}$',
                 save='mp4',  # False, 'gif', or 'mp4'
                 fps=fps,
                 preview=True,
                 w=w)