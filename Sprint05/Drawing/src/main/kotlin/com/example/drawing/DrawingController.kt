package com.example.drawing

import javafx.fxml.FXML
import javafx.scene.canvas.Canvas
import javafx.scene.canvas.GraphicsContext
import javafx.scene.control.ToggleButton
import javafx.scene.control.ToggleGroup
import javafx.scene.input.MouseEvent
import javafx.scene.paint.Color

class DrawingController {
    @FXML
    private lateinit var canvas: Canvas

    @FXML
    private lateinit var lineButton: ToggleButton

    @FXML
    private lateinit var rectButton: ToggleButton

    @FXML
    private lateinit var circleButton: ToggleButton

    private lateinit var toggleGroup: ToggleGroup

    private lateinit var gc: GraphicsContext
    private var startX = 0.0
    private var startY = 0.0

    @FXML
    fun initialize() {
        toggleGroup = ToggleGroup().apply {
            lineButton.toggleGroup = this
            rectButton.toggleGroup = this
            circleButton.toggleGroup = this
        }

        gc = canvas.graphicsContext2D

        canvas.addEventHandler(MouseEvent.MOUSE_PRESSED) { e -> onMousePressed(e.x, e.y) }
        canvas.addEventHandler(MouseEvent.MOUSE_DRAGGED) { e -> onMouseDragged(e.x, e.y) }
        canvas.addEventHandler(MouseEvent.MOUSE_RELEASED) { e -> onMouseReleased(e.x, e.y) }
    }

    private fun onMousePressed(x: Double, y: Double) {
        startX = x
        startY = y
    }

    private fun onMouseDragged(x: Double, y: Double) {
        gc.clearRect(0.0, 0.0, gc.canvas.width, gc.canvas.height)
        when ((toggleGroup.selectedToggle as ToggleButton).text) {
            "Line" -> drawLinePreview(x, y)
            "Rectangle" -> drawRectPreview(x, y)
            "Circle" -> drawCirclePreview(x, y)
        }
    }

    private fun onMouseReleased(x: Double, y: Double) {
        when ((toggleGroup.selectedToggle as ToggleButton).text) {
            "Line" -> drawLine(x, y)
            "Rectangle" -> drawRect(x, y)
            "Circle" -> drawCircle(x, y)
        }
    }

    private fun drawLine(x: Double, y: Double) {
        gc.stroke = Color.BLACK
        gc.strokeLine(startX, startY, x, y)
    }

    private fun drawRect(x: Double, y: Double) {
        gc.stroke = Color.BLACK
        gc.strokeRect(Math.min(startX, x), Math.min(startY, y), Math.abs(startX - x), Math.abs(startY - y))
    }

    private fun drawCircle(x: Double, y: Double) {
        gc.stroke = Color.BLACK
        val radius = Math.hypot(startX - x, startY - y)
        gc.strokeOval(startX - radius, startY - radius, 2 * radius, 2 * radius)
    }

    private fun drawLinePreview(x: Double, y: Double) {
        gc.stroke = Color.GRAY
        gc.strokeLine(startX, startY, x, y)
    }

    private fun drawRectPreview(x: Double, y: Double) {
        gc.stroke = Color.GRAY
        gc.strokeRect(Math.min(startX, x), Math.min(startY, y), Math.abs(startX - x), Math.abs(startY - y))
    }

    private fun drawCirclePreview(x: Double, y: Double) {
        gc.stroke = Color.GRAY
        val radius = Math.hypot(startX - x, startY - y)
        gc.strokeOval(startX - radius, startY - radius, 2 * radius, 2 * radius)
    }
}




