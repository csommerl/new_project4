document.addEventListener('DOMContentLoaded', () => {

    // functionality for like button
    const likeButtons = document.querySelectorAll('button[type="button"]');
    likeButtons.forEach(likeButton => {
        likeButton.addEventListener('click', () => {
            likeButtonClick(likeButton);
        });
    });
});

function likeButtonClick(likeButton) {
    // gets the id of the post that the button accompanies, based on the id assigned
    postID = parseInt(likeButton.id.slice(7,));
    
    // changes text of like button upon click
    if (likeButton.textContent === 'Like') {
        likeButton.textContent = 'Unlike';
        // change badge display, based on badge_id
        // add put method with AJAX
    } else {
        likeButton.textContent = 'Like';
        // change badge display, based on badge_id
        // add put method with AJAX
    };
}