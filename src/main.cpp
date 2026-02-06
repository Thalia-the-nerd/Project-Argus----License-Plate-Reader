#include <iostream>
#include <opencv2/opencv.hpp>
#include <string>

int main(int argc, char **argv) {
  // Open the default camera (ID 0)
  // You can replace 0 with a filename (e.g., "traffic_video.mp4") to test files
  cv::VideoCapture cap(0);

  if (!cap.isOpened()) {
    std::cerr << "Error: Could not open video stream." << std::endl;
    return -1;
  }

  std::cout << "========================================" << std::endl;
  std::cout << "   ARGUS EYE ONLINE: ISR FEED ACTIVE    " << std::endl;
  std::cout << "========================================" << std::endl;
  std::cout << " [q] -> Quit System" << std::endl;
  std::cout << " [s] -> Snapshot to Analysis Buffer" << std::endl;

  cv::Mat frame;

  // Counter to ensure unique filenames
  int snapshotCount = 0;

  while (true) {
    // Capture frame-by-frame
    cap >> frame;

    // If the frame is empty (end of video or camera disconnect), break
    if (frame.empty()) {
      std::cerr << "Warning: Empty frame captured. Stream ending." << std::endl;
      break;
    }

    // Display the resulting frame
    cv::imshow("Argus ALPR Feed", frame);

    // Wait for 25ms and check for key press
    char c = (char)cv::waitKey(25);

    // [q] Exit the loop
    if (c == 'q') {
      break;
    }

    // [s] Save snapshot for the Python Brain
    if (c == 's') {
      // Create a unique filename based on tick count to avoid overwrites
      std::string filename =
          "buffer/capture_" + std::to_string(cv::getTickCount()) + ".jpg";

      // Write the image to disk
      bool saved = cv::imwrite(filename, frame);

      if (saved) {
        std::cout << ">> [SENT] Frame sent to Intelligence Node: " << filename
                  << std::endl;
      } else {
        std::cerr << "!! [ERROR] Failed to save frame. Does the 'buffer' "
                     "directory exist?"
                  << std::endl;
      }
    }
  }

  // Release the video capture object and close windows
  cap.release();
  cv::destroyAllWindows();

  std::cout << "System Shutdown Complete." << std::endl;

  return 0;
}
