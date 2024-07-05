package com.example.drawing

import javafx.application.Application
import javafx.fxml.FXMLLoader
import javafx.scene.Scene
import javafx.scene.layout.BorderPane
import javafx.stage.Stage

class DrawingApp : Application() {
    override fun start(primaryStage: Stage) {
        primaryStage.title = "Drawing Application"

        val loader = FXMLLoader(javaClass.getResource("/com/example/drawing/drawing_app.fxml"))
        val root: BorderPane = loader.load()

        primaryStage.scene = Scene(root)
        primaryStage.show()
    }
}

fun main() {
    Application.launch(DrawingApp::class.java)
}

