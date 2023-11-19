# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MeshPrint
                                 A QGIS plugin
 メッシュをPDF化に変換
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-03-19
        copyright            : (C) 2021 by WilliamSebastian
        email                : s-willam@orbitalnet.jp
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MeshPrint class from file MeshPrint.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .mesh_print import MeshPrint
    return MeshPrint(iface)