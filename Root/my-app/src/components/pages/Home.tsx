import React from 'react';
import styles from './homepage.module.css';

const Home: React.FC<{}> = () => {
    return (
      <>
        <div className={styles['homepage']}>
            <div className={styles['outerBox']}>
              <h1>Welcome to CMS Open Source Metrics</h1> 
            </div>
            <div className={styles['overlay']}> </div>
          </div>
          <div className={styles['box-description']}>
          <div className={styles['description']}> 
              <h2> This site is intended for program managers and developers
              interested in learning about the status of a open source project
              </h2>
          </div>
          </div>
      </>
    )
};
export default Home;