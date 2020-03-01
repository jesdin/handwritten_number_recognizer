import 'package:flutter/material.dart';
import 'package:handwrittennumberrecognizer/constants.dart';
import 'package:handwrittennumberrecognizer/drawing_painter.dart';

class RecognizerScreen extends StatefulWidget {
  RecognizerScreen({Key key, this.title}) : super(key: key);
  final String title;

  @override
  _RecognizerScreen createState() => _RecognizerScreen();
}

class _RecognizerScreen extends State<RecognizerScreen> {
  List<Offset> points = List();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Container(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Expanded(
              flex: 1,
              child: Container(
                padding: EdgeInsets.all(16),
                color: Colors.red,
                alignment: Alignment.center,
                child: Text('Header'),
              ),
            ),
            Container(
              padding: EdgeInsets.all(16),
              color: Colors.green,
              child: CustomPaint(
                size: Size(kCanvasSize, kCanvasSize),
                painter: DrawingPainter(
                  offsetPoints: points,
                ),
              ),
            ),
            Expanded(
              flex: 1,
              child: Container(
                padding: EdgeInsets.all(16),
                color: Colors.blue,
                alignment: Alignment.center,
                child: Text('Footer'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}