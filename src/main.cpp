#include <iostream>
#include <opencv2/opencv.hpp>

int main(int argc, char **argv) {
  // Open the default camera (ID 0)
  // Change to a filename like "traffic.mp4" to test files
  cv::VideoCapture cap(0);

  if (!cap.isOpened()) {
    std::cerr << "Error: Could not open video stream." << std::endl;
    return -1;
  }

  std::cout << "Argus Core Online. Press 'q' to exit." << std::endl;

  cv::Mat frame;
  while (true) {
    // Capture frame-by-frame
    cap >> frame;

    // If the frame is empty, break immediately
    if (frame.empty())
      break;

    // Display the resulting frame
    cv::imshow("Argus ALPR Feed", frame);

    // Press 'q' on keyboard to exit
    char c = (char)cv::waitKey(25);
    if (c == 'q')
      break;
  }

  // Release the video capture object
  cap.release();
  cv::destroyAllWindows();

  return 0;
}
