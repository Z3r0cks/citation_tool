//Output:  T. Schrader. „Wissenschaftliche Texte finden, verstehen und schreiben“. Scribbr.com. https://www.scribbr.de/wissenschaftliches-schreiben/wissenschaftliche-texte/ (abgerufen 31.10.2022).

//Output whitout Author: „Wissenschaftliche Texte finden, verstehen und schreiben“. Scribbr.com. https://www.scribbr.de/wissenschaftliches-schreiben/wissenschaftliche-texte/ (abgerufen 31.10.2022).

const wrapper = document.querySelector('.wrapper');
const copyButton = document.querySelector('#copyButton');
const copyLastButton = document.querySelector('#copyLastButton');

// Author, Title, Title from website, URL, access date
// insert your citations here Set the first value to false if you want to exclude the author:

const allCitation = [
   [false, "Template Matching", "OpenCV", "https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html", "06.07.2023"],
   ["J. Malik, R. Dahiya, G. Sainarayanan", "citeseerx", "Harris Operator Corner Detection using Sliding Window Method", "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=06b419ccfb4b63efa6c64cdb971bf2e7f5d7ca47", "06.07.2023"],
   ["David G. Lowe", "University of British Columbia", "Distinctive Image Features from Scale-Invariant Keypoints", "https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf", "07.07.2023"],
   ["E. Rublee, V. Rabaud, K. Konolige, G. Bradski", "willowgarage", "ORB: an efficient alternative to SIFT or SURF", "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6126544", "07.07.2023"],
   ["D. Tyagi", "medium.com", "Introduction to FAST (Features from Accelerated Segment Test)", "https://medium.com/data-breach/introduction-to-fast-features-from-accelerated-segment-test-4ed33dde6d65", "07.07.2023"],
   ["D. Tyagi", "medium.com", "Introduction to BRIEF(Binary Robust Independent Elementary Features)", "https://medium.com/@deepanshut041/introduction-to-brief-binary-robust-independent-elementary-features-436f4a31a0e6", "07.07.2023"],
]; 

const initial = "P";

for (let i = 0; i < allCitation.length; i++) {
   const [author, title, titleFromWebsite, url, accessDate] = allCitation[i];
   const citationElement = document.createElement('div');
   citationElement.classList.add('citation');
   citationElement.innerHTML = `[${initial + (i + 1)}]
         ${author ? `<span class="author">${author}</span>. ` : ''}
         <span class="title">„${title}“</span>. 
         <span class="titleFromWebsite">${titleFromWebsite}</span>. 
         <span class="url">${url}</span> 
         <span class="accessDate"> (abgerufen: ${accessDate}).</span>
      `;
   wrapper.appendChild(citationElement);
}

copyButton.addEventListener('click', () => {
   removeTextMessage()
   let textToCopy = wrapper.textContent.replace(/\s+/g, ' ').trim();
   navigator.clipboard.writeText(textToCopy)
      .then(() => {
         addMessage('Text successfully copied to clipboard!');
         removeTextMessageWithTimeOut();
      })
      .catch(() => {
         addMessage('Text could not be copied to clipboard!');
         removeTextMessageWithTimeOut();
      });
});

function removeTextMessageWithTimeOut() {
   setTimeout(removeTextMessage, 2000);
}
function removeTextMessage() {
   if (wrapper.lastChild.classList.contains('message'))
      wrapper.removeChild(wrapper.lastChild);
}

function addMessage(message) {
   const messageEl = document.createElement('div');
   messageEl.classList.add('message');
   messageEl.textContent = message;
   wrapper.appendChild(messageEl);
}

copyLastButton.addEventListener('click', () => {
   removeTextMessage()
   let textToCopy = wrapper.lastChild.textContent.replace(/\s+/g, ' ').trim();
   navigator.clipboard.writeText(textToCopy)
      .then(() => {
         addMessage('Last text successfully copied to clipboard!');
         removeTextMessageWithTimeOut();

      })
      .catch(() => {
         addMessage('Text could not be copied to clipboard!');
         removeTextMessageWithTimeOut();
      });
});

