document.addEventListener('DOMContentLoaded', () => {

    // functionality for like button
    const likeButtons = document.querySelectorAll('.like-button');
    likeButtons.forEach(likeButton => {
        likeButton.addEventListener('click', () => {
            likeButtonClick(likeButton);
        });
    });

    // functionality for follow button
    const followButton = document.querySelector('.follow-button');
    followButton.addEventListener('click', () => {
        followButtonClick(followButton);
    });

});


function followButtonClick(followButton) {
    // gets id of profile to follow
    const profilename = followButton.id.slice(14,);
    const followerCount = document.querySelector(`#${profilename}-follower-count`)

    // what to do based on current status
    if (followButton.textContent === 'Follow') {
        
        // update button text
        followButton.textContent = 'Unfollow';
        followerCount.textContent = parseInt(followerCount.textContent) + 1;

        // update database
        fetch(`/follow/${profilename}`, {
            method: 'POST'
        });

        //// display error message?

    } else {

        // update button text
        followButton.textContent = 'Follow';
        followerCount.textContent = parseInt(followerCount.textContent) - 1;

        // update database
        fetch(`/unfollow/${profilename}`, {
            method: 'POST'
        });

        //// display error message?

    };
}


function likeButtonClick(likeButton) {
    // gets the id of the post that the button accompanies, based on the id assigned
    const postID = parseInt(likeButton.id.slice(12,));

    // Gets like badge
    const likeBadge = document.querySelector(`#like-badge-${postID}`);
    
    // what to do based on current status
    if (likeButton.textContent === 'Like') {
        
        // update like button text and badge display number
        likeButton.textContent = 'Unlike';
        likeBadge.textContent = parseInt(likeBadge.textContent) + 1;
        
        // update database
        fetch(`/like/${postID}`, {
            method: 'POST'
        });

        //// display error message?
        
    } else {
        
        likeButton.textContent = 'Like';
        likeBadge.textContent = parseInt(likeBadge.textContent) - 1;

        fetch(`/unlike/${postID}`, {
            method: 'POST'
        });
        
        //// display error message?

    };
}