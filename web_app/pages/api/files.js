import fs from 'fs';
import path from 'path';

export default function handler(req, res) {
  // Retrieve the directory from the query parameters
  const { dir = '' } = req.query;
  const directoryPath = path.join(process.cwd(), 'data_to_show', dir);

  fs.readdir(directoryPath, { withFileTypes: true }, (err, files) => {
    if (err) {
      console.log(err);
      return res.status(500).json({ message: "Unable to access directory" });
    }
    const data = files.map(file => ({
      name: file.name,
      isDirectory: file.isDirectory(),
    }));
    res.status(200).json(data);
  });
}
