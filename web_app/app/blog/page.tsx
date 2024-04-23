"use client"

import React, { Component } from "react";
import Link from "next/link";
import Image from "next/image";
import { postData } from '../data/post_images/postData'; 

export default class GridDisplay extends Component {
    render() {
        return (
            <div className="bg-lightgrey py-4" id="blog-section">
                <div className='mx-auto max-w-7xl sm:py-4 lg:px-8 '>
                  
                    <div className="text-center mb-4">
                        <h1 className="font-heading text-2xl sm:text-4xl md:text-7xl lg:text-6xl"
                            style={{
                              WebkitTextStroke: '2px black', // for Chrome, Safari
                              textStroke: '2px black', // experimental, might not be needed depending on browser support
                              color: 'transparent',
                            }}>
                              Articles
                        </h1>
                        <h3 className="text-4xl sm:text-6xl font-bold">Our latest posts.</h3>
                    </div>

                    <div className="grid grid-cols-3 gap-4 pt-4">
                        {postData.map((item, i) => (
                            <div key={i} className='bg-white m-3 p-3 shadow-lg rounded-3xl relative'>
                            <div className="relative">
                                <Image src={item.imgSrc} alt="Article image" width={400} height={300} className="m-2" />
                            </div>
                           
                            <h4 className='text-2xl font-bold pt-6 text-black'>{item.heading}</h4>
                            <h4 className='text-2xl font-bold pt-1 text-black'>{item.heading2}</h4>
                            <div className="flex items-end" style={{justifyContent:'space-between'}}>
                                <div>
                                    <h3 className='text-base font-normal pt-6 pb-2 opacity-75'>{item.authors}</h3>
                                    <h3 className='text-base font-normal pb-1 opacity-75'>{item.date}</h3>
                                </div>
                                <div>
                                <Link href={`../blog/${item.slug}`}>
                                  <h3 className="bg-black text-white py-3 px-5 text-sm rounded-full">
                                    {item.time} read
                                  </h3>
                                </Link>
                                </div>
                             </div>
                        </div>
                        
                        ))}
                    </div>
                </div>
            </div>
        );
    }
}


