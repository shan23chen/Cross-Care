'use client'

import { useState, useEffect } from 'react';

export default function Home() {
    const [files, setFiles] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        // Fetch the list of files when the component mounts
        fetch('/api/files')
            .then(response => response.json())
            .then(data => setFiles(data));
    }, []);

    return (
        <div>
            <h1>Download Files</h1>
            <input
                type="text"
                placeholder="Search files..."
                onChange={(e) => setSearchTerm(e.target.value)}
                value={searchTerm}
            />
            <ul>
                {files.filter(file => file.toLowerCase().includes(searchTerm.toLowerCase())).map(file => (
                    <li key={file}>
                        <a href={`/downloads/${file}`} download>{file}</a>
                    </li>
                ))}
            </ul>
        </div>
    );
}
