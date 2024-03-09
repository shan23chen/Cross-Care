import React from 'react';
import Image from 'next/image'; // Assuming you're using Next.js

export default function DemoPlots() {
  // Import images using require
  const raceVizImg = require('@/static_race_viz.png').default.src;
  const trendsVizImg = require('@/static_trends_viz.png').default.src;

  return (
    <section id="demo-plots" className="py-8 md:py-12 lg:py-32 bg-gray-100">
      <div className="text-center max-w-[64rem] mx-auto">
        <h2 className="text-3xl font-semibold mb-6">Our Data Visualizations</h2>
        <p className="text-lg text-gray-700 max-w-[85%] mx-auto">
          Explore our interactive visualizations showcasing key insights and
          trends derived from our comprehensive data analysis.
        </p>
      </div>

      <div className="mt-12 mx-auto max-w-[58rem]">
        {/* Trends Chart */}
        <div className="mb-16 bg-white p-6 shadow-lg rounded-lg">
          <h3 className="text-2xl font-semibold mb-4">Trends Overview</h3>
          <p className="mb-4 text-gray-600">
            Discover the evolving trends and patterns identified in our
            datasets, providing valuable insights into emerging topics and focus
            areas.
          </p>
          <Image
            src={trendsVizImg}
            alt="Trends Visualization"
            layout="responsive"
            width={700}
            height={400}
          />
        </div>

        {/* Race Distribution Chart */}
        <div className="bg-white p-6 shadow-lg rounded-lg">
          <h3 className="text-2xl font-semibold mb-4">
            Race Distribution Analysis
          </h3>
          <p className="mb-4 text-gray-600">
            A detailed breakdown of race distribution, highlighting the
            demographic diversity in our datasets and bringing attention to
            representation in health data.
          </p>
          <Image
            src={raceVizImg}
            alt="Race Distribution Visualization"
            layout="responsive"
            width={700}
            height={400}
          />
        </div>
      </div>
    </section>
  );
}
