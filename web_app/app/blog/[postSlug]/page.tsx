import { postData } from '../../data/postData';
import {
    Card,
  } from '@tremor/react';

export default function Post({
    params,
}) {
    // Assuming postData is an array and each post has an 'id' property
    const post = postData.find(post => post.slug === params.postSlug);

    // If post is not found, you can handle it gracefully
    if (!post) {
        return <h1>Post not found</h1>;
    }

    // Render the post details
    return (
        <section className="flex-col justify-center items-center space-y-6 pb-8 pt-5 md:pb-12 md:pt-5 lg:pb-32 lg:pt-5">
        <div className="flex flex-col items-center px-40">
          <Card>
         <div className="bg-lightgrey py-4" id="blog-section">
            <div className='mx-auto max-w-7xl sm:py-4 lg:px-8 '>
                <div className="text-center mb-4">
                    <h1 className="font-heading text-2xl sm:text-4xl md:text-7xl lg:text-6xl"
                        style={{
                            WebkitTextStroke: '2px black', // for Chrome, Safari
                            textStroke: '2px black', // experimental, might not be needed depending on browser support
                            color: 'transparent',
                        }}>
                            {post.heading}
                    </h1>
                    <h3 className="text-4xl sm:text-6xl font-bold">{post.heading2}</h3>
                    <p>{post.date}</p>

                </div>
                <p>{post.name}</p>
            <div className='mx-auto max-w-7xl sm:py-4 lg:px-8'>
                <article>
                    <p>{post.content}</p>
                </article>
            </div>
        </div>
        </div>
        </Card>
        </div>
      </section>
    );
}
