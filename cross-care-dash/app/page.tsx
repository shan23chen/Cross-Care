// @ts-nocheck
import React from 'react';
import Link from 'next/link';
import FeaturesSection from '../app/features';
import OpenSourceSection from '../app/open_source';
import DemoPlots from '../app/demo_plots';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faXTwitter, faLinkedinIn } from '@fortawesome/free-brands-svg-icons';

const IndexPage = () => {
  return (
    <>
      

      {/* Video Background */}
      <div className="fixed top-0 left-0 w-full h-full z-[-1] flex justify-center items-center" style={{ backgroundColor: 'black' }}>
        <video autoPlay loop muted playsInline style={{ width: '50%', height: 'auto', maxWidth: '50%', objectFit: 'cover', marginLeft: '35%', marginTop: '10%'}}>
          <source src="/videos/background.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>


      <section className="flex justify-center items-center space-y-6 pb-8 pt-6 md:pb-12 md:pt-10 lg:py-32">
        <div className="flex flex-col md:flex-row items-center text-center md:text-left max-w-[64rem] w-full gap-4">
          
          {/* Title on the Left */}
          <div style={{color: "white"}}className="flex-1">
          <h1 className="font-heading text-3xl sm:text-5xl md:text-6xl lg:text-7xl"
              style={{
                WebkitTextStroke: '2px white', // for Chrome, Safari
                textStroke: '2px white', // experimental, might not be needed depending on browser support
                color: 'transparent',
              }}>
                Cross-Care
              <span style={{ WebkitTextStroke: '0px', color: 'white' }}> Dataset</span> 
          </h1>
            <div style={{ paddingRight: "0%"}}>
              <p className="max-w-[42rem] py-4 leading-normal text-muted-foreground sm:text-xl sm:leading-8">
                The Cross-Care Dataset provides comprehensive insights into <span style={{textDecoration: "underline", textDecorationColor: "white" }} >co-occurrence patterns</span> of various diseases. This dataset is
                invaluable for researchers and healthcare professionals seeking to
                understand complex disease interactions and trends.
              </p>
            </div>
            <button className="btn mt-4" style={{ flex: 'none', backgroundColor: "gray" }}> {/* Adjust the flex property as needed */}
              <Link href="/tables">Dataset Overview</Link>
            </button>
          </div>

          {/* Social Media Icons on the Right */}
          <div className="flex-1 flex justify-end">
            <div className="flex flex-col items-center space-y-2" style={{ alignSelf: 'flex-start', paddingBottom: '50%' }}>
              
                <div
                  style={{
                    backgroundColor: 'transparent',
                    color: "#E5E4E2",
                    width: '25px'
                  }}
                ><a href="https://www.linkedin.com/school/harvard-medical-school/" target="_blank">
                  <FontAwesomeIcon icon={faLinkedinIn} /> </a>
                </div>

                <div
                  style={{
                    backgroundColor: 'transparent',
                    color: '#E5E4E2',
                    width: '25px'
                  }}
                ><a href="https://twitter.com/aim_harvard" target="_blank">
                  <FontAwesomeIcon icon={faXTwitter} /> </a>
                </div>
              
                
            </div>
          </div>

        </div>
      </section>


      {/* Features Section */}
      <FeaturesSection />

      {/* Demo plots section */}
      <DemoPlots />
      {/* Open Source Section */}
      <OpenSourceSection />
    </>
  );
};

export default IndexPage;
