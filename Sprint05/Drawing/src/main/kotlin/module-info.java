module com.example.drawing {
    requires javafx.controls;
    requires javafx.fxml;
    requires kotlin.stdlib;

    requires com.almasb.fxgl.all;

    opens com.example.drawing to javafx.fxml;
    exports com.example.drawing;
}