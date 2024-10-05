import React from 'react';

const VideoPlayer = ({ videoUrl }) => {
    return (
        <div className="video-player">
            <video
                controls
                className="w-full h-auto"
                src={videoUrl}
                type="video/mp4"
                // You can set other attributes as needed, e.g. poster image
            >
                Your browser does not support the video tag.
            </video>
            <style jsx>{`
                .video-player {
                    max-width: 800px;
                    margin: 20px auto;
                }
                video {
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
            `}</style>
        </div>
    );
};

export default VideoPlayer;
