import { NextApiRequest, NextApiResponse } from 'next';
import archiver from 'archiver';
import path from 'path';
import fs from 'fs';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { folder = '' } = req.query as { folder?: string };

  // Set the headers to inform the browser about the download
  res.setHeader('Content-Type', 'application/zip');
  res.setHeader('Content-Disposition', `attachment; filename="${path.basename(folder)}.zip"`);

  const archive = archiver('zip', {
    zlib: { level: 9 } // Set the compression level
  });

  archive.on('error', function(err) {
    res.status(500).send({ error: err.message });
  });

  // Pipe archive data to the response
  archive.pipe(res);

  const directoryPath = path.join(process.cwd(), 'public', folder);

  // Append files from a directory
  archive.directory(directoryPath, false);

  // Finalize the archive
  archive.finalize();
}
