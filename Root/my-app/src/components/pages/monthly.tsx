import React from 'react';
import styles from './monthly.module.css';
import graph from  './_graphs/overview.svg';
// import graphs from  './_graphs';
// Import the filesystem module
// const fs = require('fs');
// const folderChildren = await fs.readdir(graphs)
const Monthly: React.FC<{}> = () => {
    return (
        <>
        <div className={styles['box']}>
        <img src={graph} className={styles['overview']} alt="overview" />
            <h2> monthly</h2>

        </div>
        </>
    )
};
export default Monthly;