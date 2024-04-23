import { postData } from '../../data/post_images/postData';
import { Card } from '@tremor/react';

export default function Post({ params }) {
  const post = postData.find((post) => post.slug === params.postSlug);

  if (!post) {
    return <h1>Post not found</h1>;
  }

  // Function to create elements from content with images and URLs with optional display names
  const createContentElements = (content) => {
    const imgRegex = /!\[.*?\]\((.*?)\)/g;
    const urlRegex = /\[(.*?)\]\((https?:\/\/\S+)\)/g; // Updated regex to capture display name and URL
    let lastIndex = 0;
    const elements = [];
    let match;

    while ((match = imgRegex.exec(content)) !== null) {
      // Add text before the image
      const text = content.slice(lastIndex, match.index);
      elements.push(...createLinkElements(text, urlRegex)); // Parse URLs in the text
      // Add image element
      elements.push(<img key={`img-${match[1]}`} src={`/${match[1]}`} alt="Embedded Post" className="my-4 max-w-full mx-auto p-2" />);
      lastIndex = match.index + match[0].length;
    }

    // Add any remaining text after the last image
    const remainingText = content.slice(lastIndex);
    elements.push(...createLinkElements(remainingText, urlRegex));

    return elements;
  };

  // Helper function to replace URLs in text with anchor tags, using optional display names
  const createLinkElements = (text, regex) => {
    const elements = [];
    let lastIdx = 0;
    let urlMatch;

    while ((urlMatch = regex.exec(text)) !== null) {
      // Add previous text
      if (urlMatch.index > lastIdx) {
        elements.push(<span key={`text-${lastIdx}`}>{text.slice(lastIdx, urlMatch.index)}</span>);
      }
      // Add link element
      const displayName = urlMatch[1] || urlMatch[2]; // Use the display name if provided, otherwise use the URL
      elements.push(<a key={`link-${urlMatch[2]}`} href={urlMatch[2]} target="_blank" rel="noopener noreferrer" className="text-blue-600 ">{displayName}</a>);
      lastIdx = urlMatch.index + urlMatch[0].length;
    }

    // Add any remaining text
    if (lastIdx < text.length) {
      elements.push(<span key={`text-${lastIdx}`}>{text.slice(lastIdx)}</span>);
    }

    return elements;
  };

  const contentElements = createContentElements(post.content);
  return (
    <section className="flex-col justify-center items-center space-y-6 pb-8 pt-5 md:pb-12 md:pt-5 lg:pb-32 lg:pt-5">
      <div className="flex flex-col items-center px-40">
        <Card>
          <div className="bg-lightgrey py-4" id="blog-section">
            <div className="mx-auto max-w-7xl sm:py-4 lg:px-8">
              <div className="text-center mb-4">
                <h1
                  className="font-heading text-2xl sm:text-4xl md:text-7xl lg:text-6xl"
                  style={{
                    WebkitTextStroke: '2px black',
                    textStroke: '2px black',
                    color: 'transparent'
                  }}
                >
                  {post.heading}
                </h1>
                <h3 className="text-4xl sm:text-6xl font-bold">
                  {post.heading2}
                </h3>
                <p>{post.date}</p>
              </div>

              <div className="mx-auto max-w-7xl sm:py-4 lg:px-8">
                <h5 className="text-0.5xl sm:text-1xl" style={{ display: 'flex', alignItems: 'center' }}>
                    Written by 
                    <span className="text-0.5xl sm:text-1xl font-bold" style={{ marginLeft: '4px' }}>
                        {post.authors}
                    </span>
                </h5>

                <br />
                <article>
                  {contentElements}
                </article>
              </div>
            </div>
          </div>
        </Card>
      </div>
    </section>
  );
}
