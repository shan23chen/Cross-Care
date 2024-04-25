// components/FileExplorer.tsx
'use client'

import { useEffect, useState } from 'react';
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import FolderIcon from '@mui/icons-material/Folder';
import InsertDriveFileIcon from '@mui/icons-material/InsertDriveFile';

interface FileEntry {
  name: string;
  isDirectory: boolean;
}

interface FileExplorerProps {
  basePath?: string;
}

const FileExplorer: React.FC<FileExplorerProps> = ({ basePath = '' }) => {
  const [files, setFiles] = useState<FileEntry[]>([]);
  const [loading, setLoading] = useState(false);
  const [path, setPath] = useState(basePath);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/files?dir=${encodeURIComponent(path)}`)
      .then(response => response.json())
      .then((data: FileEntry[]) => {
        setFiles(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching files:', error);
        setLoading(false);
      });
  }, [path]);

  const handleDirectoryClick = (name: string) => {
    setPath(path => path ? `${path}/${name}` : name);
  };

  const goBack = () => {
    const newPath = path.split('/').slice(0, -1).join('/');
    setPath(newPath);
  };

  const downloadFile = (file: string) => {
    const filePath = `${window.location.origin}/${path}/${file}`;
    window.open(filePath, '_blank');
  };

  const downloadFolder = (folderName: string) => {
    const folderPath = `${path}/${folderName}`;
    const apiPath = `/api/download-folder?folder=${encodeURIComponent(folderPath)}`;
    window.location.href = apiPath;
  };

  return (
    <div>
      {path && <button onClick={goBack}>
        <ArrowBackIcon />
      </button>}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {files.map((file, index) => (
            <li className="p-2" style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              borderBottom: '1px solid #000'
            }} key={index}>
              <span onClick={() => file.isDirectory ? handleDirectoryClick(file.name) : null} style={{ display: 'flex', alignItems: 'center' }}>
                {file.isDirectory ? <FolderIcon style={{ marginRight: '8px' }} /> : <InsertDriveFileIcon style={{ marginRight: '8px' }} />}
                {file.name} {file.isDirectory ? '/' : ''}
              </span>
              <button onClick={() => file.isDirectory ? downloadFolder(file.name) : downloadFile(file.name)}>
                <FileDownloadIcon />
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>


  );
};

export default FileExplorer;
