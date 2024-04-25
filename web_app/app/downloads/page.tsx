// pages/index.tsx
"use client"
import FileExplorer from '../components/FileExplorer';

const Home: React.FC = () => {
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
                              File Explorer
                        </h1>
                        <h3 className="text-4xl sm:text-6xl font-bold">Our Data.</h3>
                    </div>

                    <div className="bg-white p-8 ">
                        <FileExplorer />
                    </div>
                </div>
            </div>
  );
}

export default Home;
