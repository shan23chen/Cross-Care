// components/Sidebar.tsx
import Link from 'next/link';

const Sidebar = () => {
  return (
    <div className="w-1/5 h-screen flex flex-col bg-gray-100 border-r-2 border-gray-300">
      <ul className="p-5 text-left mx-auto">
        {/* Main category title */}
        <li className="font-medium">
          <p className="py-2 font-semibold">Getting Started</p>
          <ul className="space-y-1 p-4">
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/getting-started/installation"
              >
                Installation
              </Link>
            </li>
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/getting-started/navigating-results"
              >
                Navigating Results
              </Link>
            </li>
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/getting-started/related-work"
              >
                Related work
              </Link>
            </li>
          </ul>
        </li>
        <li className="font-medium">
          <p className="py-2 font-semibold">Co-occurrences</p>
          <ul className="space-y-1 p-4">
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/co-occurrences/pretraining-bias"
              >
                Pretraining Bias
              </Link>
            </li>
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/co-occurrences/pretraining-datasets"
              >
                Pretraining Datasets
              </Link>
            </li>
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/co-occurrences/methods"
              >
                Methods
              </Link>
            </li>
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/co-occurrences/results"
              >
                Results
              </Link>
            </li>
          </ul>
        </li>
        <li className="font-medium">
          <p className="py-2 font-semibold">Cross Care</p>
          <ul className="space-y-1 p-4">
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/cross-care/user-guide"
              >
                User Guide
              </Link>
            </li>
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/cross-care/downloads"
              >
                Downloads
              </Link>
            </li>
            <li>
              <Link
                className="text-gray-900 hover:text-blue-600 font-medium block py-2 px-4 rounded transition duration-150 ease-in-out"
                href="/docs/cross-care/examples"
              >
                Cross Care Examples
              </Link>
            </li>
          </ul>
        </li>
        {/* Additional sections */}
      </ul>
    </div>
  );
};

export default Sidebar;
