// OpenSourceSection.tsx
import React from 'react';
import Link from 'next/link';

const OpenSourceSection: React.FC = () => {
  return (
    <section className="flex justify-center items-center space-y-6 pb-8 pt-6 md:pb-12 md:pt-10 lg:py-32">
      <div style={{color: "white"}}className="flex flex-col items-center text-center max-w-[64rem] w-full gap-4">
        <h2 className="font-heading text-3xl leading-[1.1] sm:text-3xl md:text-6xl">
          Proudly Open Source
        </h2>
        <p className="max-w-[85%] leading-normal  text-muted-foreground sm:text-lg sm:leading-7">
          Our project is open source and powered by open source software. <br />
          The code is available on{' '}
          <Link
            href="https://github.com/shan23chen/Cross-Care"
            className="hover:text-blue-600"
          >
            GitHub
          </Link>
          .
        </p>
      </div>
    </section>
  );
};

export default OpenSourceSection;
