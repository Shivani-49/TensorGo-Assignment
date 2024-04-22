import cv2

def convert_video(input_path, output_path):
    # Open the input video file
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    # Get input video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create VideoWriter object to save the output video
    # Change fourcc parameter to 'mp4v' for MP4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output_path, fourcc, fps, (1280, 720))

    # Process each frame of the input video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Resize the frame to HD resolution (1280x720)
        frame_hd = cv2.resize(frame, (1280, 720))

        # Write the resized frame to the output video
        out.write(frame_hd)

        # Display progress
        print("Processed frame: {}/{}".format(int(cap.get(cv2.CAP_PROP_POS_FRAMES)), total_frames), end='\r')

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage
input_video_path = 'E:/input_video.mp4'
output_video_path = 'E:/output_video.avi'
convert_video(input_video_path, output_video_path)
