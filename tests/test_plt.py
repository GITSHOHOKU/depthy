import unittest
import numpy as np
import matplotlib.pyplot as plt

from depthy.misc import plot_point_cloud


class PlotDepthTestCase(unittest.TestCase):

    def setUp(self):

        self.plot_opt = False

    def test_point_cloud(self):

        # test invalid downscale parameters
        for i in range(-1, 1):
            try:
                plot_point_cloud(disp_arr=None, rgb_img=None, down_scale=i)
            except IndexError as e:
                self.assertTrue(e, IndexError)

        # test case where rgb image missing
        plot_point_cloud(disp_arr=np.ones([3, 3]), rgb_img=None, down_scale=1)

        # test case for image dimension mismatch
        plot_point_cloud(disp_arr=np.ones([6, 6]), rgb_img=np.ones([3, 3, 3]), down_scale=1)

        # test valid case
        plot_point_cloud(disp_arr=np.ones([6, 6]), rgb_img=np.ones([6, 6, 3]), down_scale=2)

        # test Axes3D argument
        fig, ax = plt.figure(), plt.axes(projection='3d')
        ax_type = type(ax)
        ax = plot_point_cloud(disp_arr=np.ones([6, 6]), rgb_img=np.ones([6, 6, 3]), view_angles=(50, 70), ax=ax)
        self.assertEqual(type(ax), ax_type, msg='Expected %s type, but got %s' % (ax_type, type(ax)))

    def test_all(self):

        self.test_point_cloud()
