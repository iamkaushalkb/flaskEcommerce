-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: bmz
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookproduct`
--

DROP TABLE IF EXISTS `bookproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `bookproduct` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `date` datetime NOT NULL,
  `no_of_products` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookproduct`
--

LOCK TABLES `bookproduct` WRITE;
/*!40000 ALTER TABLE `bookproduct` DISABLE KEYS */;
INSERT INTO `bookproduct` VALUES (1,'yashasvi','yashasvi@gmail.cum','9806682290','pokhara','apple','iphone11pro','2020-07-06 04:13:16',NULL),(2,'Kaushal Kumar Bhattarai','iamkaushalkb@gmail.com','987654321','Pokhara','SAMSUNG','Samsung S9','2020-07-21 11:49:31',2),(3,'John','john@business.com','986754321','Pokhara','XIAOMI','Samsung S9','2020-07-21 12:03:32',5);
/*!40000 ALTER TABLE `bookproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `contact` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cname` varchar(255) NOT NULL,
  `cemail` varchar(255) NOT NULL,
  `csubject` varchar(255) NOT NULL,
  `cmsg` varchar(255) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,'Kaushal','iamkaushalkb@gmail.com','Demo','Demo','2020-05-22 15:13:04'),(2,'Tony','tony@business.com','Regarding Business','Hi.','2020-05-22 15:13:04'),(7,'Kaushal','iamkaushalkb@gmail.com','Business','Hi','2020-07-21 12:08:02'),(9,'Kaushd','sdgf@fsdfg','louyg7t8','dfsfs','2020-07-29 10:42:15');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `img` varchar(255) NOT NULL,
  `feedback` varchar(255) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (19,'Kaushal','i','LRM_EXPORT_20200513_190518_1.jpg','Nice','2020-07-17 12:10:55'),(22,'Tony','tony@business.com','LRM_EXPORT_20200124_115950.jpg','Nice','2020-07-17 14:26:30'),(23,'Jenish','jenish@business.com','LRM_EXPORT_20200124_200205.jpg','Hi','2020-07-18 23:00:11'),(24,'Yashasvi','ssv@gmail.com','puspa_2.jpg','fdsfs','2020-07-29 11:08:26'),(25,'John Doe','john@gmail.com','blank-avatar_1.webp','Nice Shop','2020-07-29 12:14:16'),(27,'Mark Dollitle','mark@gmail.com','blank-avatar_3.webp','Nice Service','2020-07-29 12:15:48'),(28,'Susan','susan@gmail.com','blank-avatar_4.webp','Nice Environment ','2020-07-29 12:16:37');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `tagline` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `content` longtext,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (3,'Rising Star of Juventus','Cristiano Ronaldo','cr7','Cristiano Ronaldo dos Santos Aveiro GOIH ComM (European Portuguese: [kɾiʃˈtjɐnu ʁɔˈnaɫdu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for Serie A club Juventus and captains the Portugal national team. Often consid','2020-05-24 20:46:13'),(4,'Birth Place Of Legends','Nepal','nepal','Nepal (Nepali: नेपाल [neˈpal]), officially the Federal Democratic Republic of Nepal,[14] is a country in South Asia. It is located mainly in the Himalayas, but also includes parts of the Indo-Gangetic Plain. It is the 49th largest country by population an','2020-05-24 20:48:13'),(13,'A OnePlus Nord ','OnePlus Nord','one-plus-nord-blog','<p>OnePlus Nord&nbsp;was announced last week, but the Nord phone is just the first Nord product in a line that is yet to come. So if you\'re wondering what the next device in the newly established family is going to be, well, it looks like it\'s also a phone. Shocking, we know.</p>\r\n<p>Unlike the first Nord, that\'s limited in availability to Europe and India (at least for now), the next Nord will make it to North American markets too, according to CEO Carl Pei speaking to&nbsp;<em>Wired</em>. The timeline for the launch is \"later this year\".</p>\r\n<p>That handset may be powered by the recently unveiled&nbsp;<a href=\"https://www.gsmarena.com/qualcomm_announces_snapdragon_690_chipset-news-43803.php\">Snapdragon 690</a>&nbsp;chipset, Qualcomm\'s soon-to-be cheapest offering with 5G. The chip maker needs to go down in price from the 765/768 family (also used in the Nord), in order to compete better with MediaTek\'s Dimensity 800/820.</p>\r\n<p>Thus, the next OnePlus Nord may be even cheaper than the current Nord. And be available in the US. The SoC information comes from some digging into the latest version of OxygenOS 10.5 for the Nord, performed by the folks at&nbsp;<em>XDA-Developers</em>.</p>\r\n<p>They found several references to an upcoming OnePlus smartphone codenamed Billie, as well as multiple calls to a method called \"isSM6350Products\" in the OxygenOS Settings app. SM6350, incidentally, is Qualcomm\'s internal designation of the Snapdragon 690. That method checks the model of the device and returns true if it matches BE2025, BE2026, BE2028, or BE2029.</p>\r\n<p>Those are all versions of the same upcoming model, based on OnePlus\' usual naming scheme, where \"BE\" could stand for Billie Eilish. That\'s not as crazy as it sounds - the current Nord\'s AC2001 and AC2003 model numbers have the \"AC\" standing for Avicii, so the music star theme is pretty real in OnePlus\' codename game.</p>\r\n<p>\" &gt;</p>','2020-07-29 12:12:37'),(14,'Realme V5 tours','Realme','realme-blog','<p>days away&nbsp;from launch, but before the full reveal we\'re getting even more teasers. The latest features the phone photographed at various locations. Every shot shows the back with that large &ldquo;realme&rdquo; label.</p>\r\n<p>Those aren&rsquo;t random locations, by the way, the V5 took a tour of colleges and universities. Realme is specifically targeting Generation Z with this phone.</p>\r\n<p>Based on official teasers, this will be a 5G phone with a 48MP main camera. Less official sources add a few more details: a 6.5&rdquo; 1080p+ LCD, 5,000 mAh battery with 30W fast charging and a 16MP selfie camera.</p>\r\n<p>The chipset remains a bit of a mystery. One of the teasers boasts about its 5G capabilities and mentions that it&rsquo;s a 7 nm chip. However, both the Snapdragon 765G and Dimensity 800 match that description (as well as the unconfirmed 2.0 GHz clock speed for the CPU).</p>','2020-07-29 12:11:05'),(15,'Google','Google is now price-matching in 23 overseas markets','google-blog','<p>Google has been offering price-matching in the United States, but now the company is expanding the service outside of its home country and will now reach 23 more markets. It will allow customers to buy anything from the Google Store and if they find a lower price in selected retailers, they&rsquo;ll get a discount to match that price.</p>\r\n<p>Key retailers that Google has highlighted are MediaMarkt, Carrefour, Amazon, and Argos, but it is different for every country - check out the Source link for a qualifying retailer for each country. There&rsquo;s also an explanation of how the price matching works, including that it works for Unlocked devices only and must be the same color and memory option.</p>\r\n<p>The full list of updated markets includes&nbsp;<em>Australia, Austria, Belgium, Canada, Denmark, Finland, France, Germany, Ireland, Italy, Japan, Netherlands, New Zealand, Norway, Portugal, Puerto Rico, Singapore, South Korea, Spain, Sweden, Switzerland, Taiwan, and the United Kingdom</em>.</p>','2020-07-29 12:12:08');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `price` int NOT NULL,
  `description` longtext,
  `img` varchar(100) DEFAULT NULL,
  `slug` varchar(255) NOT NULL,
  `date` datetime NOT NULL,
  `imgb` varchar(255) DEFAULT NULL,
  `imgc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (2,'XIAOMI','MI A2',15000,'<p><strong>The Mi A2 from Xiaomi is a part of Google\'s Android One Program. It sports a 5.99-inch display with fullHD+ resolution and Corning Gorilla Glass 5 for protection. It is powered by a Snapdragon 660 processor, has 4GB of RAM and 64GB of internal storage. The Xiaomi Mi A2 has a metal unibody design and a 3000mAh battery. It has a USB Type-C port at the bottom and an IR Blaster at the top. The Xiaomi Mi A2 runs stock Android 8.1 Oreo. It has a dual camera setup at the back consisting of a 12-megapixel primary camera and a 20-megapixel secondary camera. The smartphone also has support for Qualcomm\'s Quick Charge 4+. It is a dual SIM device with support for 4G and VoLTE on both slots.</strong></p>','mia2.webp','mia2','2020-07-29 11:32:31',NULL,NULL),(3,'XIAOMI','Redmi note 8 pro',25000,'<p><strong>Redmi Note 8 Pro is a highly sought after smartphone. It has a big-display which measures 6.53-inches and a water drop notch that houses the selfie camera. The display also has support for HDR.&nbsp; It has a glass back that is made out of Corning Gorilla Glass 5. The Redmi Note 8 pro also has an IR Blaster at the top whihc cna be used to control other IR-based appliances.</strong></p>\r\n<p><strong>The Redmi Note 8 Pro is powered by the MediaTek Helio G90T which is a gaming processor. It is very capable and can play most gaming title out there on the play store. There are three variants of the Redmi Note 8 Pro, 6GB RAM with 64GB storage, 6GB RAM with 128GB storage and 8GB RAM with 128GB storage. It uses UFS 2.1 for storage and has a dedicated card slot for storage expansion.</strong></p>\r\n<p><strong>Xiaomi ships the Redmi Note 8 Pro with MIUI 10 running on top of Android 9 Pie. It comes preinstalled with a few apps which are capable of generating spammy notifications. The Redmi Note 8 Pro packs in a 4,500mAh battery that helps the device deliver good battery life. Xiaomi has also bundled an 18W charger with the device. The Redmi Note 8 Pro packs a triple camera setup at the back and clicks some good shots in different lighting conditions. We found low-light video performance to be sub-par.</strong></p>','Redmi_note_8_pro.jpeg','redmi-note-8-pro','2020-07-29 11:34:50',NULL,NULL),(6,'APPLE','Iphone11 Pro Max',150000,'<p><strong>The biggest iPhone in Apple\'s lineup, the iPhone 11 Pro Max looks like an incremental upgrade over the iPhone XS Max but it brings some significant changes under the hood. There\'s a triple camera setup at the back now, letting you choose between the Wide, Ultra Wide, and Telephoto lenses.</strong></p>\r\n<p><strong>The Camera app makes it seamless to pick one or the other, presenting the Ultra Wide camera as a 0.5x zoom, which is certainly an interesting perspective. All this is backed by improved HDR and a brand new Night Mode, which means you get excellent image and video quality in most conditions. For the first time in years, Apple\'s phones not only compete, but often surpass the competition in terms of low light photography.</strong></p>\r\n<p><strong>An area where Apple\'s dominance has never really been in doubt has been chip design, and the new Apple A13 Bionic chip continues this tradition. From intensive gaming sessions to editing 4K videos on the go, iPhone 11 Pro Max will handle everything you throw at it with ease, and then some.</strong></p>\r\n<p><strong>There are significant gains to be had in the battery life department as well, and even users with the heaviest of workloads shouldn\'t have a problem lasting a full day. Most typical users will find the iPhone 11 Pro Max is, in fact, capable of lasting up to two days on a single charge. iOS 13 brings a host of new features and the promise of regular software updates.</strong></p>\r\n<p><strong>So what\'s not to like? Looking beyond that camera module, the price is an obvious deterrent. What\'s more, despite paying over a lakh, you get a measly 64GB of internal storage. We also wish Apple adds software features like picture-in-picture that make better use of the big screen.</strong></p>','11promax.jpeg','iphone-11-pro-max','2020-07-29 11:41:19',NULL,NULL),(7,'APPLE','Iphone 11',100000,'<ul>\r\n<li><span class=\"a-list-item\">6.1-inch Liquid Retina HD LCD display</span></li>\r\n<li class=\"qa-bullet-point-list-element\" style=\"text-align: left;\"><span class=\"a-list-item\">Water and dust resistant (2 meters for up to 30 minutes, IP68)</span></li>\r\n<li class=\"qa-bullet-point-list-element\"><span class=\"a-list-item\">Dual-camera system with 12MP Ultra Wide and Wide cameras; Night mode, Portrait mode, and 4K video up to 60fps</span></li>\r\n<li class=\"qa-bullet-point-list-element\"><span class=\"a-list-item\">12MP TrueDepth front camera with Portrait mode, 4K video, and Slo-Mo</span></li>\r\n<li class=\"qa-bullet-point-list-element\"><span class=\"a-list-item\">Face ID for secure authentication and Apple Pay</span></li>\r\n<li class=\"qa-bullet-point-list-element\"><span class=\"a-list-item\">A13 Bionic chip with third-generation Neural Engine</span></li>\r\n<li class=\"qa-bullet-point-list-element\"><span class=\"a-list-item\">Fast charge with 18W adapter included</span></li>\r\n<li><span class=\"a-list-item\">Wireless charging</span></li>\r\n</ul>','iphone11f_1_1.jpeg','iphone-11','2020-07-21 11:55:59',NULL,NULL),(8,'XIAOMI','MI A3',25000,'<p><strong>The Mi A3 is the third smartphone in the series of Android One smartphones from Xiaomi. It sports a 6.08-inch display with HD+ resolution. We found this to be low considering that the predecessors of this device, the Mi A1 and the Mi A2 had full HD+ panels.</strong></p>\r\n<p><strong>The display puts out less than 300 pixels per inch and the device does not let you tweak the colour settings of the display. We found the panel to be slightly boosted for our liking. The Mi A3 is powered by a Qualcomm Snapdragon 665 SoC and comes in two variants,&nbsp;4GB RAM with 64GB of storage and 6GB RAM with 128GB of storage. You do have the option to expand storage further as the phone has a hybrid dual-SIM slot.&nbsp;</strong></p>\r\n<p><strong>We found the Snapdragon 665 to be powerful enough to handle day-to-day tasks and also games like PUBG Mobile without any lag or stutter. The Mi A3 packs in a 4,030mAh battery and has a USB Type-C port. It delivered good battery life and we could go on for close to a day and a half without needing to be charged. Xiaomi claims that the Mi A3 has support for 18W fast charging but it only gets a 10W charger in the box.</strong></p>\r\n<p><strong>Xiaomi offers a triple camera setup on the Mi A3 consisting of a 48-megapixel primary sensor, an 8-megapixel ultra-wide angle sensor with a 118-degree field-of-view, and a 2-megapixel depth sensor. At the front, it has a 32-megapixel selfie shooter. We found the camera performance to be quite good in different lighting conditions.</strong></p>','mia3.png','mi-a3','2020-07-29 11:42:35',NULL,NULL),(9,'APPLE','Iphone SE 2020',80000,'<p><strong>The iPhone SE (2020) is an unusual device, combining a throwback style with some modern internal components. It\'s virtually identical to the iPhone 8 from the outside, and there aren\'t many phones these days that are as slim and light. That also means the screen is small, at 4.7 inches, and battery life isn\'t great. You get the modern A13 Bionic processor which is extremely powerful, but only a single rear camera. The main attraction for many people will be iOS, which is smooth and slick, with multiple years of updates guaranteed. Apple also targets this phone at those who want to upgrade from an older model to continue using iCloud services.&nbsp;</strong></p>\r\n<p><strong>While you can get good performance from the iPhone SE (2020), its utility is limited by the small screen. The rear camera takes great stills and video in the daytime, but low-light performance is disappointing. Noteworthy features include wireless charging and an IP67 water resistance rating.</strong></p>\r\n<p><strong>There are plenty of Android models at around the same price which offer much more competitive core specifications, but iPhone users will be glad to have the option of a more affordable&nbsp;model.&nbsp;</strong></p>','iphonse.jpg','iphone-se-2020','2020-07-29 11:44:32',NULL,NULL),(10,'APPLE','Iphone XS',130000,'<p><strong>Apple iPhone XS smartphone was launched in September 2018. The phone comes with a 5.80-inch touchscreen display with a resolution of 1125x2436 pixels at a pixel density of 458 pixels per inch (ppi). Apple iPhone XS is powered by a hexa-core Apple A12 Bionic processor. The Apple iPhone XS supports wireless charging, as well as proprietary fast charging.</strong></p>\r\n<p><strong>As far as the cameras are concerned, the Apple iPhone XS on the rear packs a 12-megapixel primary camera with an f/1.8 aperture and a pixel size of 1.4-micron and a second 12-megapixel camera with an f/2.4 aperture. The rear camera setup has autofocus. It sports a 7-megapixel camera on the front for selfies, with an f/2.2 aperture.</strong></p>\r\n<p><strong>Apple iPhone XS based on iOS 12 and packs 64GB of inbuilt storage. The Apple iPhone XS is a dual-SIM (GSM and GSM) smartphone that accepts Nano-SIM and eSIM cards. The Apple iPhone XS measures 143.60 x 70.90 x 7.70mm (height x width x thickness) and weighs 177.00 grams. It was launched in Gold, Silver, and Space Grey colours. It features an IP68 rating for dust and water protection.</strong></p>\r\n<p><strong>Connectivity options on the Apple iPhone XS include Wi-Fi 802.11 a/b/g/n/ac, GPS, Bluetooth v5.00, NFC, Lightning, 3G, and 4G (with support for Band 40 used by some LTE networks in India) with active 4G on both SIM cards. Sensors on the phone include accelerometer, ambient light sensor, barometer, gyroscope, proximity sensor, and compass/ magnetometer. The Apple iPhone XS supports face unlock with 3D face recognition.</strong></p>','iphonexs.jpg','iphone-xs','2020-07-29 11:48:58',NULL,NULL),(11,'APPLE','Iphone XR',90000,'<p><strong>Apple iPhone XR smartphone was launched in September 2018. The phone comes with a 6.10-inch touchscreen display with a resolution of 828x1792 pixels at a pixel density of 326 pixels per inch (ppi) and an aspect ratio of 19.5:9. Apple iPhone XR is powered by a hexa-core Apple A12 Bionic processor. It comes with 3GB of RAM. The Apple iPhone XR runs iOS 12 and is powered by a 2942mAh non-removable battery. The Apple iPhone XR supports wireless charging, as well as proprietary fast charging.</strong></p>\r\n<p><strong>As far as the cameras are concerned, the Apple iPhone XR on the rear packs a 12-megapixel camera with an f/1.8 aperture. The rear camera setup has autofocus. It sports a 7-megapixel camera on the front for selfies, with an f/2.2 aperture.</strong></p>\r\n<p><strong>Apple iPhone XR based on iOS 12 and packs 64GB of inbuilt storage. The Apple iPhone XR is a dual-SIM (GSM and GSM) smartphone that accepts Nano-SIM and eSIM cards. The Apple iPhone XR measures 150.90 x 75.70 x 8.30mm (height x width x thickness) and weighs 194.00 grams. It was launched in Black, Blue, Coral, Red, White, and Yellow colours. It features an IP67 rating for dust and water protection.</strong></p>\r\n<p><strong>Connectivity options on the Apple iPhone XR include Wi-Fi 802.11 a/b/g/n/ac, GPS, Bluetooth v5.00, NFC, Lightning, 3G, and 4G (with support for Band 40 used by some LTE networks in India) with active 4G on both SIM cards. Sensors on the phone include accelerometer, ambient light sensor, barometer, gyroscope, proximity sensor, and compass/ magnetometer. The Apple iPhone XR supports face unlock with 3D face recognition.</strong></p>','iphonexr.jpg','iphone-xr','2020-07-29 11:57:20',NULL,NULL),(12,'SAMSUNG','Samsung S9 ',100000,'<p><strong>The Samsung Galaxy S9 features a metal and glass design, with tapering edges on both sides. It has a 5.8-inch Quad HD+ Super AMOLED display with an 18.5:9 aspect ratio. Touch response and colours are superb and it also supports HDR. In India, the phone uses an Exynos 9810 octa-core SoC and comes with 4GB of RAM a choice of 64GB or 256GB internal storage, which is expandable. The stereo speakers delivers good sound quality and there\'s wireless charging here too. The main highlight is the camera, which features a variable aperture, super slow motion videos up to 960fps and AR Emojis. Camera performance is good too, especially in low light. The 3000mAh battery supports fast charging and should stretch an entire day on a single charge.</strong></p>','s9e.jpg','samsung-s9','2020-07-29 11:56:44',NULL,NULL),(13,'SAMSUNG','Samsung Galaxy Note 8',100000,'<p><strong>The Samsung Galaxy Note 8 is slightly taller and heavier than the S8+, but simply feels better built and more solid in your hand. The 6.3-inch Quad HD+ display is gorgeous and produces excellent contrast. The S-Pen now has a finer tip and is IP68 certified. You can use it to create hand-drawn GIFs, translate words, and search the web with Bixby Vision. This phone is powerful too thanks to the Exynos 9 Octa SoC and 6GB of RAM. The dual rear cameras are a first for the company and let you do things like Live Focus, which adds a pleasing bokeh effect behind your subject. The main sensor delivers excellent detail, both in daylight and at night. Battery life could have been better and we struggled to get a full day&rsquo;s worth of usage out of each full charge.</strong></p>','note.jpg','samsung-galaxy-note-8','2020-07-29 11:59:35',NULL,NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(255) NOT NULL,
  `no_of_mobiles` int NOT NULL,
  `total_sales` int NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,'APPLE',7,700000,'2020-07-13 09:41:06'),(2,'XIAOMI',10,150000,'2020-07-13 09:49:32'),(3,'XIAOMI',7,70000,'2020-07-14 12:39:26'),(4,'SAMSUNG',5,200000,'2020-07-21 11:58:15'),(5,'XIAOMI',5,50000,'2020-07-21 11:58:53'),(6,'APPLE',6,60000,'2020-07-21 11:59:04'),(7,'SAMSUNG',2,200000,'2020-07-21 11:59:18'),(8,'XIAOMI',2,30000,'2020-07-21 11:59:58'),(9,'XIAOMI',70,700000,'2020-07-21 12:00:52'),(10,'APPLE',6,600000,'2020-07-21 12:01:57'),(11,'APPLE',6,600000,'2020-07-29 11:06:04');
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-29 12:19:52
