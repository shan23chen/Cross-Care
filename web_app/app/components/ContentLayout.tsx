// @ts-nocheck
import Sidebar from './Sidebar';

const ContentLayout: React.FC = ({ children }) => {
  return (
    <div className="flex">
      <Sidebar />
      <main className="flex-1 p-10">{children}</main>
    </div>
  );
};

export default ContentLayout;
