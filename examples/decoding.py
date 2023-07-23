import json

from xal import decode_xal


extracted_xal = "78128f6159d7f17c5dc111f38f94108b90b367358c8b3eaf63fdc614e1f1a45477518478158ab63c1d814bb0cbfc4bdcd1943f6fd89834a661e1ca57bca59b052f12846943d8cb7c4cdd1cbfc1e957ddd7a1363fd7cd32ad66b3d656aab0e3436c539c6552dee02c17c85ae992bf0a8bc0fa2c098bce6abc3abfc414e7bc98487642c94d47d9f72e6ad215f888eb078d81af7b34968978bc16a18d03a8dba04a6643cb2415c2f16848c10af889e95cccc0bd22788cc872f534b0900ffabefb5c21459a6d45eff56948dd0cbfc1e92b8198a96236838631b263f1cc2de9ffa849775f9a600c90dd6059d614bdb6aa05cead932e02c29834c362e4bb57a1bc8057735c8c5f52d2df67599c4daecce555d8c2e84512b6e448b073bd8d0bedbc8642605b862117f3fc7c42de1db2cafa54c0d2ee3e74d28957fd35b09609a7a9f2102d03df2a1b92e4624cc71ef289a644d4c08d6f39abc770f93ff3c842e4fdaf4076518e6d158ab66b439e3fdfd9e7448283ae692f83ce61ef71ebbf42edf2ec604112b42415d8f57c49c419ef9e9405818ca37b2890cc6aff2af3de51b8b0e3436646806b52eff96b40dc0ae4d9f15ec2c0b07c3586dc67e871ebc627edffaa48211ccb7845dff07b4ec727ee8ea944d4c0f23e6ad19935ac64f3c842fef9af436c42cb3215f7fb614adf1dbdb2a505c0c0ec2c2c87c760f3218e9715eabefb05211ccb7f52d2f07c44c51defd9f1008f8eb36b76c0c465e40ca58b15ebf49e576c59877c4492ae3e01911bf294a00f8bbda5603b80c561f871eb9012fdf9ed057342867852c2e07772df11ee8fe95cb5c0b66b3486c676cf26b3c64caaecb34867458a7c64c5f62c01910ef895af099cc0ec2c3783d150f326b28c30e7f5af537012c52a44d3fc6b49c614f495ac44c2c0b57d3f90e867e83aa78514e1f3af052f128d6779dfe05a5fd21bf6d9e7448987af623581c870f53cbfc64caaffae496d558a7c5edffa2c019108f18eac0f8091e222788fc069f907a89405fbbeed0573548f5e5ed5e36b5ff616fc99a7038ac0ec2c2d87cb6ff52785810df8f3b3467149ba7c58c2f569489154bf8cae04858bb45e3f90da6def27b48a14dbe8ae5562578c2a1b92fc6f5fd70ffc89ae25818ca37b2890cc6aff2af3c842ebf3ae4c6a55ac6656d2f86b499154bf9abb16ad8da46b1483c461be7ff38510f8d2a04a6612c52a56c0e45848c10bf494a544c2c0b0623b96cf6bee3ef3c842f8eeae4376539d2a1b92e17d48c139fa9ea512cccee2623b8cce71fd34b4c64caaf0a0496445886f52c3b6220fdc16d192a503cccee2793f80cd76f525b49642a4bea6427777886552c0f56a5e9154bf91aa108fa7ae6f388ecc60be7ff39705e6f8834262538666159cb67844d10afc8fae44c2c0a2622f87dd6bf327b9c64caaffad4e7352866945d4b6220fd00af89fae089a8ba16229c08526f736a8860fe9eea5052f12846959d1f36b499154bf96ae028783846b2c8bca61ef71fdc613fcf3b3466455cb2415c3f17c5bda1bf8aca4148587b22c76c0df6dee27a4850cc3f9b8456c519b6c159cb6794cd81dd194a80dcccee26a3f94c067f91eb4890ffae5e30b21598763159cb66644d75ab1d9a7098d89b32c76c0c461f83ab0a701f8fda34e6f599d6152c3b6220fde1df992aa358b91b367358c8b28be23b4960de1efb24e6c5e9a2a1b92e47c48c01df38faa12878dae2c76c0da61ee3ab08842a4beb4546112c52a40d9fa6a42c43bf295bf14818eb3412c87db68fd2af3c842f0eee30b21459a6d45f1f36b43c73cfc8faa44c2c0a3623f83db45ec23938504eff9e30b21578c7c75d1e07a48c101bfd7e9018b96957d3f90e461f83ab0c64caaeea45676559a7c7af9d0476cd01bf888b844c2c0b26b2b97cc77e81eb48009e9d7a45e50499a7c52ddd56d4ed60beed9e7449d87b44f2a92eb65f834b4c64caaeba44568599d4f52c4c17d48c135f89fa207cccee2693f96e06aef27b0880cedf893426f519d6d53f1e47e5e9154bf89ae018791b46b28b2db6be83cb28b0cc0fdaf436f559b2a1b92e1605fd61ff488bf039cb2b2612e8dca6bf01bb08a04e4f9b3055e1ccb6b58defa6b4ec711f29594149a96e2346bd29979b071a68102d7fbad05394bcb6b56dee26f5eec1ef495ac039c92b26734968b3ee771bd810eefe8a9053903df3d0088b82c43c615c298a40a8190b32c60d79d3daa7ff38904bdbefb056007df3e5385a63a1dd61bfcc8ad54d7dba26d62839937ff36e7d751b9adf616211ccb7c5bc3fc2c179148a5bdf920dfda843a1ba4eb3ca567e1d457bfd9f5164702da4c0085a5381ff139dcc2f85edca7843a6ea79d3dac6490d526bfdaf2114072aa3c7289d53e6cf73ca9ce8857abc0bd227892c876fd3eb49005faefe31d78129b6d59d4f17c48c15aa7d98a28a9ae852e72a3d974f036fdc421f8ecad42237ddb2867c2fb220dfc08f8958c2aced6ee3f73c08526ea36bf800ffabefb05445f866f5bd5b44743d056bdd38a169e8ea527789fd428be24b88a04e7ebe31d7812856754d1e06742dd5aa780e9099c8ba76734c09326f427a59413b2b3ee507447c76d47d9f7694cde1deed5a80983c0ec2c2a83dd6cf232bc8142b2beee4e671f856750d9fa2148c311fed9e7448690a56878d88b6ce827a1975aa7b3b650741e8c785ed3f36f40d60bb398a40bc18ba421368dce6df27cb49409ebbebc0b2158807b43dfe6770f8903bf97ae088996a82c60d0d428be20b29605edf2e31d7812887e56d9f85145d611fa93bf44d4dbf53e76c0c872fd3abdbb17e1f8b54f210ad83d0682b82c4cc519f49794128192e23469d08526f436b88308fcbefb1e3b02c52a40d9f07a459142accefa54c2c0a361368ddb5bf836a19008aaa6f2177e1ccb7852c2f2615fde19f398ae44d499e2633f8fc676e571eb9f42e2ef9e4f6651995744d9ee6b72df11f092bf44d4d6f2376ed59931ad66e3c842fcf3b5466f6f837b68d8f16f5dec0bf481ae44d4d6f3386bd39c31a97ff39113edf89e4d706f816d56c0cb7d44c91dbfc1f950dfd4f53f6bd3d428be21b4970ffdeea2427012d35315d8e07a5dc042b2d4b8128f96a96d7783da77f927a2c910faf3a509765e9b6d56dcf1604ada16f8d5a80983cda16d398ddc6ae87ea18b12fcfdad087044887c5ed3bb7d59d20cf498e40c9dcdf3203eda9132fd30e3d14eebf4b449681e837b159cb66659c708eec1e4499d96a17a33818465ef20b49013a5ecb348671e9c6645d5f56248dd1ff495ae488d8dad213b81ca6be93da5c910e7eeb5466f1f9a7c56c4fd6d02c00cfc8fa205c188b3213783c06ab262e2d253bdf8f6102d53817d59dbba645e9154bf93bf129e91fa217596db65ff38b88a07a6f9b14e6057886552c3ba6d42de57e989aa05858bae697488da26b071b99014f8effb082c439d6943d9f7234cc00bf88fb84b9e90af6a7497c776f932bd810eeff5af422d53866518d1f76d42c616e9d6bb099c96a1627591dd65e83ab2cb13fcfdb54e601f8a7b449fa0201fd24eafcaff51d9cca3662f8cc22aff20a2c64caaf4b5537343d32718c3e06f59da1bb09ab8158b96b3232a90c660b226bf9605e9f0a4496459876d19d3fb6302d21bfe94be089acfb0612896c868b320a58514e1ffee5477519d61549ffe7d028756abcdad52dddaf33b7481c171f238ff8e13aab0e34f7744997b0d9fbb7d59d20cf498e6079d91a57a29cfd976f337ff910efaf9a04b665e8e6159d5ba6d42de57fc98a8099b8cb4232a8ddb70fd3ffe9714e9e8a8442c439d6943d9f72147c057ed94a71f888bac6229cc9861ac63b48255ecb2a24f765e82265dc3b6220fdb0ce98bb85cc1cdb7792dcccc74f530b6850dedefef446c5dc661539ff57e449c0af88bbe128f96a96134c08526f427a59413b2b3ee507447c76d47d9f7694cde1deed5a80983cda96a7583d96db33fbe8701fcf5ae49211ccb6043c4e47d179c57ea8cbc488b92a96d3d83c461ef7db28b0da7f5a508624080275e81ac6012dd0ba096ae159d83a76b29c08526f427a59413b2b3ee507447c76d47d9f7694cde1deed5a80983cda96a7583d96db33ae0dc0eb7f2b21a6640806b1ad3fb605ed616e9d6af0f8f8eaf6978ce8b6ce827a1975aa7b3b650741e8c785ed3f36f40d60bb398a40bc18ba4213b92c02bf562e98a5fe6effc4273598a2554dffa7d48dd0cb09fa207828da72c76c0c170e823a2de4fa7ebb6502d55996154d7f56348c056fe94a6498786ef6f2a8b866dad6bbfdb0efba1ac427043886f52c3b6220fdb0ce98bb85cc1cdb7792dcccc74f530b6850dedefef446c5dc661539ff57e449c19f39aa71f9a8ba37d78ce8b6ce827a1975aa7b3b2536244806b1ad1e77d48c70bb08bb9098accb5602887c868f93db68d0eedb2a2486e1f886b54dfe160599e08f289bf0782cdb37a3b96c067b336a18d03a5faa0516a5386661a89a276148556ed95ac44c2c0a87a2e92da3eb37ca59601ebf7a849641e8c785ed3f36f40d60bb398a40bc196b26f39898774f234ee9605eef9b3556a5e8e5d45dca96042dd1dbb97a4058f96a96134dfc170e823a2c153c9b9f3612602af7f40c7ba6b5dda1bfa9aa6039dcca36137c79b42f537f4d626e4f3a64e6d15db4e52c0fd6d0bdd17eac6fa50d7d2f13c6fd29930ad65e1c205fef9af535749996d0ac0f56948e511f88ce94acc8ab47a2a91932bb324a6934eedeca8446451846d449ef761409c11f9d4aa1687cda1603b8ed070f530a2c64caaf4b5537343d32718c7e37903d608f498ac078387b320398dc42bf537fe8510e1b3a049625c907c5ed3e72c019110e98fbb15d4cdef792d958761ec3ab28301e5f9b209605f84275ed4bb6f5dda57fc8ebf0e8b8cb4673983dd61be7ff38c14fcecb21d2c1f9a7c56c4fd6d00d20bee9ebf15c392b2613eccdc6aee36b08805e6fba849661e8a675a9ff56d4edc0df38fe6168190b46f36cdda70fd27b8874fedeca8442e56887e5ed3fb60008a4ee5c2fd489e8ca72c76c0c170e823a2de4fa7ebb6502d55996154d7f56348c056fe94a6498786ef6f2a8b8665f232bd9d14e1ffb2052f12817c43c0e734029c0fea8ce5039e8ba3693b8fcc77b230be894fe1f8ee467359c66959d1f87759da1beed9e7448696b47e29d8862bef27b09009ebb1a05470559d7b1ac0e661499d0df389ae078287ae69338ccc2aff3cbccb01ebffae526d44c47858c2e06f419c0be99abf0f8dcdb37a3b96c067b339a2cb54b1b2a3113205df3f0283ba6d45c616f6d5a115cccee2662e96d977a67cfe9714e9e8a8442e519a7b52c4e7235dc117f9d5be089c87a1623f8cce6df236ff870fe5b3a044605f9c66439de4615fc719f1d4b8128f96a96d7591dd65e83ab2cb0afbb3f0102d03d93000d1f6681c9d1bf58ea50dc088b32c76c0c170e823a2de4fa7e8a04b6c5ec47f52d2e76759d655ed89a402c087a3612987ca2af33dff8110e1ffa6466e559a2654dff92159d214f29594158a89ee6429c08526f427a59413b2b3ee53625c86661ac3f17c5bda1bf8d6bb148186ee6b398dda61ff7dbe8a4eedeca8446451846d449ef761409c0eacd4a2088796e222788add70ec20ebcb4fe2efef4f6051997c54d8f5204edc15b2cae4079e8bee6429ddc66af03cb0805de0dfa057775381697bdff56a48d75eef9ea5028b90fd6b2292c56dff3aa5c64caaf4b5537343d32718def1794cc00bf88fb8488681a17e2e81c165b230be894febfdb153605888274181bb68498348ffc9aa499d96a17a3381866cff32a19003e0fdef4f775d852b51c2f563488e1bf59aa70a8b8ca76b7c8bcd39ac6aa1870dfff7a41e60098e2e5fdfe77a10c40fead5ae168781a76f3787da2aff3cbcc213edf2b5557a0d9d7a42d5b27c48c317ef8faa1687dfa87a2e92da21af12f4d626adae87466053867d59c4e72045d019ed8fa80e8fcca36137c4db61ff32a19003e0fda2486e40887c0ac4e67b48951be888bf0983dfa66f3691cc22f43fec810eaee8b14b6a5e827b0adffa285eda0cf890ae1fd3dbf16b6ed39a33fa7ee8d101eeb1f5456009c43100d1f2234ed71bf89fa803dcd3a33639c4dd6cf93eb4d904e9eeaa017059936d0ad9fa7844c011ff97ae408d8aa1623687c763f97eb28b0efcfda8496642d46068d3f57e59d010fca4a80e8f8eac6b3485cc5bf03cb68d0ed7ecb3486716867a5ed7fd6010db0ce98bb843dda3e53c1cc79b42eb24a6ca05f8f5a240625d8c7b19d3fb630f9f5af58fbf169dd8ef213487de65ef20b49013a6f4a24673448a60569ef761409c1bfc8bbf058683ef786bcdcf60ac63b3d601a7efb54677598a275fd3f57e59d010fcd5a312838ee3682883c461a130b98103e3feae5f25598d350789e46d40c413f8c2a85f89c4a86129969473eb24ff8110e1ffa6466e559a2654dff9285ed616e989b25b9a90b56b7c90cc74f321a58510e1a1a95377409a2d04f1b13c6b964adb9aa8058197ae7a29ccc167fd23a58708e9b2a2486e169b6d54d1e47a4edb19fe94a6168f96fd7a2897cc22ff26a2900fe5a1a7466f438c2e5fdca96b43950ced97a2088591fd6134c4da6de836ba8119b5a5f0423701da3f519dad3b4cd555a999a85fc3dbf76f3ccfca60ff36b58705baada21f60169d6052ddf13349d20af6ddb80f9487fd673494c077f531bd8146ebf4a04b6f55876f529df76143c719f495ae14d38a9f6d3b92dd67f4328e8708e9f0ad426d578c575bdff36743ec08ef94af408190a969338c946ce827a19745bbdde4154515db4e40c7e32048c311fe9caa0b8b91ee6d358f8b28be3ba59010fba6ee0877518567599de76b5fc511fe9ee6169c8da4203f81c677f930ff8b0ea6f9b14e6057886552c3ba6d42de57ebcae4168683b36b28cdcb65e830b9c64caaf4b5537343d32718c4f56242dd55ee9eb9108781a5232a90c660b236b28b13edffef486d1e8c785ed3f36f40d60bb398a40bc194f121338cc070b336a98103fde8a4052f12817c43c0e734029c0cfc97a408c391a57c2c8bca61b123a38b04a6f9a24870558a2658deba6b5dda1bfa9aa6039dcca36137cddf35b323b98513edeeee4562448a6015ede9220fd71deb92a803b192a9763f8ef676fd27b88b42b2aeed0567519b6368ddfb6a489142e989be03c2c0a366288dc461be69a59615edb0e357715f996d45c4ed5141da0be9d9f13dccd2e22278d38b28be24b88a04e7ebe30b21438c645192b82c49dc1be896ae089ac0ec2c3483c461be7ff3880febfdb54e6c5ecb2415d3e17d59dc15d897ae0b8b8cb47d78ce8b6cf520a58b12f1beed056d519f6150d1e06742dd5ab1d9a7098d83b467358ccb65ee71fdc60dedf2b4456242cb2415c0f17c5edc16fc97a9079cc0ec2c2981db6bf03fb38512fbbeed057044887c42c3f66f5f9154bf8fa4098280a17c78ce8b77e832a59113aab0e3446f5f9a6d5392b82c4bc119f09eb844c2c0ac6b3485dd6cbe7ff3900ff8beed056c408c6652c2b6220fc319ef9ea512cccee2682883c461d93fb48905e6e8e30b215e887e5ed7f57a42c15ab1d9a4148785a96078ce8b61e427b4960ee9f0e30b21438a7a52d5fa2c019111f395ae14b98ba47a32c08526f53dbf8112c0f9a8406b44cb2415c3f77c42df14c5d9e7449e83a76b02adcf62ef36a5c64caaefa2556c5c8551159cb67e4cd41dc4b4ad009d87b42c76c0df6def26b08836e1f9b6576c429d2a1b92e76d5fd61df3a3e94acc91a37c3f87c75dbe7ff38b15fcf9b3706a549d60159cb66158c71defb3ae0f898ab42c76c0cd61ea3ab28130e1e4a44b51519d615892b82c4edf11f895bf2f8084af7c3783dd6df33df3c842fbffb342665ea56d51c4b6220fc01bef9eae08ba8db02c76c0da70e53fb4a905ecf5a0052f12866644d5f57c4edb5ab1d9a215bd87a37b2887ea6bf227b49c14aab0e35371459a7c52d4c0775dd60bbfd7e9168b90a661288fc86aff36f3c842e7f2a0577359877b43d1f86248d75ab1d9a4088c87a6612887c06aef27b0880cf8eeae4a7344cb2415d3e6775dc717bfd7e90f8086a5763f86ed46be7ff39705fbefa8486d639d6745d1f36b0f9f5af194a80782b1b4612883ce61be7ff38b0eeaf9a7487155917a44d5f86b4ec75ab1d9a4088f80af7c2ec08526f33db38106e7eea44e6d409c7c159cb66143d114e889e94acc8dae6d3b8cca61f071fdc60fe6ffa049735c8871159cb66143d019f38ba7079796a87c3597ce6cbe7ff38b0eebf4a0496455cb2415dffa6d41da1bf6d9e744818ca3623591cc26b071be8a03e7f2b5427b44856744c4b6220fdc16fe94a5128b9ab4633f8cdc26b071be8a03e7f2b5427b449b6d44c4fb7c48d75ab1d9a4088d97a56d3283c763f971fdc60fe6f8a34b605c806b5c92b82c42dd1cef9aac44c2c0af603e90c863f93db5c64caaf3af4371518e6d59c4f17c0f9f5af295af148f85ac6b3b94cc26b071be8a04fafda64875559b2a1b92fb6049c119fa88bf079c96e222788dc760ee3ca1c64caaf3af437642887c5edffa6d45d216fa9ee94acc8dae6b3792dd6df937f3c842e7f2a44967558d2a1b92fb6048c10af289e94acc8dae683581dc77be7ff38b0eeef3b34a67519d69159cb66143da16ed8ebf44c2c0af60338cdf65f03ab5c64caaf3af4c66498d6740deb6220fdc16f69eb2169c87b37d78ce8b6bf238b49d15f8beed056c5e856756d4b6220fdc16f194aa028b86a46f2e838b28be3cbf880fe9f8a4436e559d6953d1e06f0f9f5af295a7098f86b37a3b90dd26b071be8a0de7e9b242675f9e66159cb66143de17e888ae038096a57c78ce8b6bf23ebe9113edf0a4467555cb2415dffa6342c60bf896a4108bc0ec2c358cc46be920b48b15fcbeed056c5e846742c3f1615bd60abfd7e909808faf7b2987dc74be7ff38b0ee5f3b4546647816d52dcb6220fdc16ed9abe158bc0ec2c358cd968fd2af3c842e7f2b14b624980665092b82c42dd08ef94ac148b91b32c76c0c66aee32a58103e0fdaf406612c52a58dee66b5ed60cbfd7e9098090a57d3398cc26b071be8a13ebeeae4b6f12c52a58dee76b4ec60af48fb216818ea96d2394c06bf032a58d0fe6beed056c5e9a6d52dbf16a0f9f5af295b8038b89a9603dc08526f33da2810cedffb5052f12866644dcfb7a4edb19f39cae44c2c0af602996c868f036b5c64caaf3af54765284614392b82c42dd0be888bb038086e222788dc770f53eb49110ecfdb542211ccb6759c4fb694adf1dbfd7e9098094af622f8fcc67f432bf8305aab0e3486d47886143d9fa690f9f5af295bc038c89a97a3b8cc069fd27b88b0eedf2a5052f12866640d5f66544c719f392a6079a8baf603396cc76fd27b88b0eaab0e3486d478c6a5cd9e06f43da15fc8fa2098091b46f28968b28be3cbf9305eaf7a8537742886644d9e06742dd1df39fe94acc8dae793287cc68be7ff38b0ee9e9b9446f598a63159cb66143d417e98ba40f8096a57c3983d970e921b4c64caaf3af4b6c439d7858d9fa7a48c11bfc8bbf139c87e222788dc774f33abf9005faf8ae506d12c52a58dee46144dd0cf889a6099887e222788dc774f33abf9005faeea05076408d6943d5b6220fdc16ed94a2089a87b27b2ac08526f33da18b09e6e8a4556051876b52dcb6220fdc16ed94a2089a87b2612c87db26b071be8a10e7f5af536642867d4392b82c42dd08f292a5128b90a5602e87db26b071be8a10e7f5af536642856d56c6f12c019117f388ae0a8b81b47d2e83db70be7ff38b0efbf9ad426044806759d3fc6f43d41dbfd7e9098083ae673783dd6df33db48a04aab0e3486d5187615ad1e06742dd11e99eb9079a8baf6078ce8b6bf232bf8d0de9e8a8486d439d6945c4b6220fdc16e989aa089d8bb467358cdb71f271fdc60fe6e8b3466d43807c5edffa7d59d20ae9d9e744818cb47c3b8cda6de83abe8a05e6f8e30b215f877c45d1fa7d44c711f295a8078081a56278ce8b6bf232b79005faecb34e6d44cb2415dffa6c48d517ef9ebb14878cb42c76c0c66afe36b78b12ede9af4b6c518d2a1b92fb6045d20bf598a3078085a52c76c0c66af032bf8315e9fba4446b51876f5292b82c42dd15f888b8078987e222788dc769f920a28507edf9b3556c42cb2415dffa614bd514f495ae44c2c0af60358cc56df236f3c842e7f2b1466455816153d5b6220fdc16ed9aac039d8aaf7978ce8b6bf223be9413fcfdb542211ccb6759c2f16448d00cf494a50e8f8ca4623f868b28be3cbf9714e7eea0406612c52a58dee16045d216f997ae029c87aa6b3996c06bf271fdc60fe6e9af4b6c518d2a1b92f77c42c00bd289a201878c897d358ec870f937f3c842fbffa9426745856d4592b82c4cdf1def8fe94acc83b46138c08526fe3fa49642a4bea3536c51cb2415d3f5604ed614dc95a20b8f96a96134a4db65f136f3c842ebfdaf44665ca06c5bd5d76f41df1afc98a044c2c0a36f2a96dc76f916a7810efcefe30b2153856d56c2dd6059d60aeb9aa744c2c0a3623f83db50f53eb48b15fcbeed05605c867b5292b82c4edc16fb92b90bcccee26d2887c870f91abc8507eddea8536e51992a1b92f26b59d010bfd7e900878ca42c76c0cf6bff26a2c64caafba453405f847842c4f16a7ec701f19ee94acc85a57a0987c561ff27b88b0eaab0e34a62448a607ad5f0674c9154bf96a4108ba0b92c76c0c46bea36858b42a4beae57665ecb2415c0fb7d59fe1dee88aa018bc0ec2c2a90c06ae871fdc610faf3ac577712c52a46c5f17b48fe11fe89a4128f91ab2c76c0db61f036b09705cdeaa4497743cb2415c2f17e42c10cd889b9099cc0ec2c2887d871f920a5a50ee1f1a0536a5f874e45d1f96b0f9f5aef9eba138b91b4473e8ecc47fd3fbd8601ebf7e30b21428c7b5ecaf14c549154bf89ae158798a55a35c08526ef30a38b0ce4beed0570539b675bdcd6770f9f5aee98b909828e946178ce8b77f927988a14edeeb7466f12c52a44d5e05a44de1df28ebf44c2c0b37a35928b28be20a59615ebe8b4556654aa6458def12c01910ff899a00f9aa1a1603987c545f23abc8514e1f3af617151846d159cb67948d113f48f99039f97a57d2ea3c76df132a58d0fe6dab3466e55cb2415d3fc7c42de1dbfd7e9059c87a46b3496c065f03fb49713aab0e3446253816d4492b82c4edc17f692ae359a8db26b78ce8b6bf237b49209ebf9ac4877598666159cb66143d71deb92a8038190a96b3496c870f53cbfc64caaf3af436646806b52dfe66748dd0cfc8fa2098083a27d358edc70f971fdc60ce9e9af446b619c6d42d5b6220fdc16ff9ead099c87ad6f2e81c126b071b68114dbffb342665ead6d43d1fd625e9154bf8abe039c9b8c613983c542f33da59742a4beb24f6c47ad6145d5f77a42c101cd92a80d8b90e2227891c16beb1ca1810ecef5ad4253598a6352c2b6220fc010f28c9807988786673687f96dff38b49642a4beae556a57806676d7f16059f014e888bf039cc0ec2c2992cc61ff3b829d0efcf4a4546a43cb2415dffa6d42dd0cf895bf108791a96c338ec070e532a4900ffbe8a0536653816959d7f12c019117ed9ea5228f96a16c3b91cc26b071a68102e3f5b57566419c6d44c4d26741d62be488bf0383c0ec2c2d87cb6ff527838113e7f0b7424f5f8a695bf6fd6248e001ee8fae0bbbb08c2c76c0cd61fa3abf8142a4bea4536b559b6d42ddb6220ff208edb2a50f9ac0ec2c0587d96dff16bf8502e4f982486c5b806d70c5f57c499154bfa494129c83a365338cce5bfe32a28142a4beb6426140886b5cfae76143c319fe98a4138096b0612896c868b13dbe8005a5eba44570599d6d159cb67c48d41df39eb9079a8db25c2f8cdd6df136f3c842bafaf0466053df6b04d1a23e1bd148a5c9ae538b87a63b3fd79d30ad67b78202aab0e3785c63ac4663e2cd51729154bfa49407968baf7d138cda70fd3db28142a4be9e78605f9b6d1adae7515edb19ef9eaf39b1c0ec2c398ddb61be7ff3bb3fe9e4a8487079877b43d1fa6d48f019fe93ae02cccee2471783da6fbe7ff3bb3ffbe8ae556612c52a44d5e04740de1df992aa128bc0ec2c398ecc65ee1abc8905ecf5a0536612c52a68d5e4674ee70afc98a00f808583613589c061d83cbc8509e6d5a5052f12b66d47d9f75a5fd21bf692a501ad8db5602e90d047f337b4c64caac3a4576a53bd7a56d3ff6743d45ab1d9b9038d83b07a398ac84bec27b88b0efbbeed056200b6384f89ad364f9154bf9afb39de9af73662d18b28be1abf900cd8f3ad5e65598564159cb67a4cdf17f3d9e74486a1a17e2e81c165d03cb08005ecbeed056b73887843d3fc6f7fd619f982e94accb0a1783f8c8b28be3bb28510fcffa946211ccb6f45d5f76f5dc71bf59ae94acc89e222788b8b28be0794a930c7ce80755a12c52a67f5c65d64e02cd8b59f44c2c0a16a3ea7df61f2279d8d13fcf9af427112c52a53d9e77e4cc71bf5bebd038096e2227890cc69f325b4a116edf2b56b6a439d6d59d5e62c70ce54bf9faa128bc0fa757896c069f929be8a05d7f3a74170559d2a0d9da53c1d9f5afb94b90b8f96e23421c0ca65f036bf8001fabefb0564428c6f58c2ed2c01911cfc82e95cccd0ed6a3385c070be7ff3880febfdad42210acb6d599dd34c0f9f5af094a51286c0fa2c68cfcd6dfb3aa5c64caaf2b44a61559b6159d7cb7d54c00cf896e95ccc8ea17a34c08526e83abc813ff2f3af42210acb4d42c2fb7e489c2ffc89b80799c0ec2c2387c876be69f38a15e5f9b34e601294751b92e67b43c711f09ee95c95c0b36a0590cc67e921a28142b2faa04b7055942415d6e4645e9142e6d9bd039c91a96134c09326af7de2ca56aab0e3516a43807c58c2cb67499142bfcefa5fdad4f26d68819932a467b78252b8a5f2413401d83c0482a068158741a4d9e7448d8dae683386cc6aff36f3de50a6a9ed056b519a6052c3b63456911ef295bf15ccd8e23f38da9d65f867b3d303b9aff01337518c6c5380a43b4e804fad9dfd518cd2f62c76c0d968e934b88a13aaa6e3106156d03a0187f06a49d64ffcc8f853dddbf23a6e83cb3cfa35b4dd52bff8f4052f12887d53d9fb2c17911aaac9a804de84f56b6bd29062f967b5d557eefea0456203d9695389f06a4ed15ab1d9a8078094a17d78d88b30ae31e3d559b9f8f1456501db6e5284a7361e811afccff356dc83f33f69869926b071a28712edf9af0539128b6d01d4f13d1f831ba9cefd508887f16b6a81c836ff35e5d452b9f8f2443006cb754a9cb66342c711f295e95c95c0ad612f91cc69f325b4c65ad3e7e353210adb3d0688ba381d8348adcbfb54dddaf43c76c0d126a66be4dd4caae5e31d3000d0751bcbb67a0f894aa8cdf948d7d2f03e6ad29937a964e7d74caae4e31d3b05dd2415c9b6341e8248e0d7b0449ac0fa3c6fda9f2aa563e1d450b8acf2123406da2415c8b63415864db1d9b244d4d1f13e27ced226e871ebd656bfaeef163300d9380780a63d15874ab1d9b344d4daf53b76c0d026a660e0d41da4e7e353210adb3f0384b82c559142a5cefd4acc9be23469d39979b028f39042b2aef6113b1edb380780a43e1d874fabc3f851c2c0b82c60da9c3db071a8c65abbacf85a2f4bcb7c158aa238188056a9cbfb56ded2f03d6fd59f37b071a9c65abfacf30b2149cb320280ac7301c85ae9d9f150d9d2f3206dd29934ac63e1d057bea4f50b2148cb320188ac220fca5aa7cefa5093cebb2c2ec09332ab61e7ca58b8acf1173300d8390e82a5220fcb5aa7ccfb55c2c0b92c60d79833e17faac614aaa6f8123609c7300780a43e1d8349acc2f957c2c0b82c60d59935b071a8c65abca8f45a2f4bcb7c158aad381c8356a5cbfb56ded2f03f6bdb9b35b071a9c65abda8f90b2149cb320381a47301c85ae9d9f15fd8d4f02062d29934ac63e1d551b1aef00b2148cb320382a1220fca5aa7c8f35293cebb2c2ec0933dab62e1ca58b8acf1173300d8390e82a5220fcb5aa7c8f851c2c0b92c60d19c33e17faac614aaa6f8103500c7300780a43e1d8349acc2f957c2c0b82c60d09035b071a8c65abbaff25a2f4bcb7c158aad361d8a56a5cbfb56ded2f03f6bdb9b35b071a9c65abaa4f50b2149cb320482a37301c85ae9d9f15fd6d7f82063d29934ac63e1d755bfaaf20b2148cb320588a6220fca5aa7c8f95293cebb2c2ec0933da562e3ca59b8acf1173300da3d0086a7220fcb5aa7c9f357c2c0b92c60d19b30e17faac614aaa6f81e3502c7300780a43e1d8349acc2f957c2c0b82c60d09132b071a8c65abbaef95a2f4bcb7c158aad37158456a5cbfb56ded2f03f6bdb9b35b071a9c65abbacf70b2149cb320484a67301c85ae9d9f157ded3f03c74d19934ac63e1d451b9a5f3162f12912a0d84ad39019101bfc1ff56da9fec7578968b3ead63e0d152a6a4f1173300d9380681ad3c1c9f5ae5d9f150dcd0ec2c23c09330af67acc81baae8e31d3200d830039eac3e1d8348adcbfa57d7d0f122789a8b3eab63e3c842f1befb13360194244c92e02c178249adcefa48dfd2f03e6ad29936af6be5d64caae4e31d3400da2415c9b634198b4ce0d7b0449ac0fa3f6bd39935b26be1d450b8acf1163209db391b92ec2c17864fabd7e91fccd8f43e639f857fbe27f3de51b9adf4162d08d9380780a43e1c8241afcae74496c0fa3a6cd08526e571ebd754bbe1ed5c2144cb320681a5371a9d41adcbfb56ded2f33b6dd49a28be2bf3de54bba9ed057a12d33b0586e92256910cbfc1fa57dcd2f3206fce8b7cbe69e5d755a4beb8053903db3e4a9cef2c599142accaf856dfccf83e6ad29934ac62e0dd52b9b0e35f210add3b039cb6770f894bafcdb64a95c0b42c60d39837ad67ffd550b8acf1173302da300382b82c559142a9c8ff4acc9be23469d09f79b028f39042b2adf51f3200c7310780a43e1d834ba8ccfd55c2c0b82c60d69a30b071a8c65abbaef75a2f4bcb7c158aa53a158549b3c2fb56ded2f03e69d79e32af7ff39c42b2a8f2152f12902a0d83a23e509f03bf8fe95cdfd6f93f6bcc9134ac63e1d450b9adf815321ccb70158aa03f1a9f5ae4d9f155d8d7bd2221c0dd26a662e5dd52b9b2f9173300d9380781a5371f8254bf83e95cdad3f522789b8b3eaf65e4994cf3beb5053901dc380582ba3f1d8348adcbfb54dddaf43c76c0d126a667e0d14caae5e31d3006dc751bcbb67a0f8949a8cbfc53c0daf03e6ad29934ad62e8d651a4beb9053904d83d1b92ed2c17804eab86e71dcc96e2346bd79836a97de8d450b8acf1173005de3e049cb6760f894cacc8e74497c0fa3d62d1d428e771a5c65ab9a9f0133b1ed0380780a43e1d804daacdf84acc9ae2346ed39a28be2af3de53b0aabc0b78129d2a0d81a13d1d8a54bf83e95cdad3f322789b8b3eaf6be7994cf3beb5053901dc3b0282ba371d8348adcbfb55dbd5f63d76c0d126a667e0d74caae5e31d3008d1751bcbb67a0f8949a8cef853c0daf03e6ad29934ad62e8d651a4beb9053904d83b1b92ed2c178040a486e71dcc96e2346bd79c3caa7de9d450b8acf1173201d03a069cb6760f894cadcae74497c0fa3a6bd2d428e771a5c65ab9a9f714301ed1380780a43e1d8249a4c9fa4acc9ae2346ed29c28be2af3de54bda5bc0b78129d2a0d81a138158556a5cbfb56ded2f03f6bdb9b35b071a9c65abcacf80b2149cb320280a17301c85ae9d9f157dbd5f33b74da9934ac63e1d451b9a5f3162f12912a0d84a53d019101bfc1fe55df9fec7578968b3ead66e6dc57a6aef1173300d9380387a236199f5ae5d9f152dfd6ec2c23c09331a862acc81baae8e31d3205d13b039ead3e1d8348adcbf853d9d4f322789a8b3ea862e4c842f1befb12370694244c92e02c17824eaccafb48d6d2f03e6ad29935ad6ae3d54caae4e31d3500de2415c9b634188641e0d7b0449ac0fa3f6cd39f36b26be1d450b8acf1163209db391b92ec2c178448aed7e91fccd8f53b6c9f857fbe27f3de51beaef81f2d08d9380780a43e1c8241afcae74496c0fa396ad18526e571ebd154b8e1ed5c2144cb320686a73a149d40adcbfb56ded2f13f63d09828be2bf3de56bdafed057a12d33d0380e92256910cbfc1fa50dddbf82063d29934ac63e1d755bfaaf20b2148cb320184a4220fca5aa7ceff5093cebb2c2ec09335aa67e5dd4eb0acf1173300d9390689a6220fcb5aa7cdf357c2c0b92c60d79d30e17faac614aaa6f0113706d0260f80a43e1d8348accaf254c2c0b82c60d59937b071a8c65abdaff85a5e1ccb6558c5e76b49dc0ff3d9f13d95c0b42c60db9135ac7de9d450b8acf1173201d03a069cb6760f894aa5cfe74497c0fa3d68d5d428e771a5c65ab9adf01f301ed1380780a43e1d8249a4c9fa4acc9ae2346ed19028be2af3de53baa4bc0b78129d2a0d81a13f1d8556a4cbfb56ded2f03d6fd59f37b071a9c65abcadf50b2149cb320487a17301c85ae9d9f157dbdaf63d74d39934ac63e1d452bba4f5152f12912a0d84a53b019101bfc1fe52d89f9d22788fc671ef36a49442b2c7ba057712d3310f88ac20148348adcbfb56ddd7f73869ce8b7cbe69e3dc52a4beb8053903db3c4a9cef2c599142accaf953dcccf33e6ad29934ac62e0dd52b9b0e35f210add3b029cb6770f894bafcdb64a95c0b42c60d39c35a567ffd650b8acf1173304de3e0f84b82c559142a9caf84acc9be23469da9f79b028f39042b2adf41e3703c7390780a43e1d834aaec3ff54c2c0b82c60d69831b071a8c65abda8f75a5e1ccb7f5fd5f1620f8923c0d7e9128197a3662996c876e871ebbf3da4beb5487653816d59d4b63476ee54bf8fa4138d8aad612c878b3ec70efdc613ebeeae4b6f12d3536a9cb66548ca1cf28ca544d4b9bb2c2ec09335ad60e0d44eb1acf1173300d93b0287a23d509f03bf8fe95cdfd3f33a68cc9d34ac63e1d450bba9f611304dc57315c4b6341c824babc9e55393cebb2c2ec09335ad67e6d31da4e7e353210ad8390388a1201a8348adcbfb56dad5f6366e9f857fbe27f3de51b9a8f9122d07d9380780a43e19844ea5cfb64a95c0b42c60d39832ab67ffd350b8acf1173304de3e0f84e92256910cbfc1fa57d8dbf4206dd29934ac63e1d057bea4f55a2f4bcb7c158aa53f158a40b3c2fb56ded2f03e69d79e32af2efd9f42fcbefb163209d93a1982a43e1d8348adcffc50d6d6bd2221c0dd26a662e3d450b1b2f45a2f4bcb7c158aa53c1d8a4cb3c3fb56ded2f03e6bd39036ad2efd9f42fcbefb163105d83e4a9cef2c599142acc9fd54dfccf57376998b70be69e0d657baabef1e3300d9380780a73b1a854be0d7b0449ac0fa3f68db9d34b26ae1d450b8acf1143607df3b4a9cef2c599142acc8fb57d8ccf13e6ad29934ac61e2dc54bae1ed5c2144cb320683a53d1d9d4cadcbfb56ded2f33b6dd49a79b028f39042b2adf2103004c7390780a43e1d834aaec3ff5493cebb2c2ec09335af6ae3d01da4e7e353210ad83c0787a020198348adcbfb56ddd7f738699f857fbe27f3de51bcadf8112d01d9380780a43e1f8040a9c9b64a95c0b42c60d39d36aa6bffd550b8acf1173302da300382e92256910cbfc1fa52dddbf52069d29934ac63e1d551b1aef05a2f4bcb7c158aa53b1e864cb3c9fb56ded2f03e6ed59f3ca82efd9f42fcbefb163603d0301987a43e1d8348adcffc50d6d6bd2221c0dd26a662e4d050beb2f5173300d9380783a1391b8005b180e912ccd8f13b6fd6992aae63e1d450b8acf5103508dd751bcbb67a0f8949a8cefe54c0d6f03e6ad29934af66e6d253f5b0ba057712d3390285a236038048adcbfb56ded3f13768d3d428e771a5c65ab9a9f6173a1edb380780a43e1d874fabc3ff1bc299e27a78d89831ab62e3ca59b8acf1173300da3d0086a77301c85ae9d9f157dbd5f23f74da9934ac63e1d451b9a5f3167e6dc52a5cd5ed7b5d9142c680e912ccd8f13f69db902aad63e1d450b8acf3143b04db751bcbb67a0f8949accffb54c0d1f03e6ad29934ad62e8d651f5b0ba057712d3390684a438038548adcbfb56ded0f3366ed0d428e771a5c65ab9adf412311edd380780a43e1d804daacdf81bc299e27a78d89835a966e7ca51b8acf1173300db3b0f84a67301c85ae9d9f157dfd7f63b74d39934ac63e1d452bba4f5157e1c922a4392ae3f1c844da8d5fa56ded2f03e6ad09a3ca861acc81baae8e31d3201de3d0f9ea23e1d8348adcbf955d6d6f27376998b70be69e0d559bcaaef103300d9380780a0391b8b4ce0d7b0449ac0fa3f6bdb9c34b26be1d450b8acf1163209db394a9cef2c599142acc9fb52dcccf43e6ad29934ac60e4d356bbe1ed5c2144cb320682a5381a9d4badcbfb56ded2f13f63d09879b028f39042b2adf3123708c73b0780a43e1d8349acc2f95793cebb2c2ec09335ae65e6dc4ebbacf1173300d9390689a63f509f03bf8fe95cdfd0f83e6acc9c79b028f39042b2adf31e3a07c73b0780a43e1d8349acc2f95793cebb2c2ec09335af63e9d44ebeacf1173300d93a0488a03c509f03bf8fe95cdfd1f1396ecc9a34ac63e1d450b9adf815324dc57315c4b6341c804fa5c9e555ded2f03e6ad29835a561e0994cf3beb5053901da310f84ba3b509f03bf8fe95cdfd6f13d6b9f857fbe27f3de51bcaef5102d06d9380780a43e1f8040a9c9b64a95c0b42c60d39d37ad61ffd350b8acf1173304de3e0f84e92256910cbfc1fa52dad4f4206ed29934ac63e1d755bfaaf25a2f4bcb7c158aa53b19864cb3c2fb56ded2f03e69d79e32af2efd9f42fcbefb163604dc301987a43e1d8348adcffc50d6d6bd2221c0dd26a662e4d056bab2f8173300d9380783a1391b8005b180e912ccd8f13b6cd39b2aae63e1d450b8acf5103508dd751bcbb67a0f8949a8cdf952c0d6f03e6ad29934af66e6d253f5b0ba057712d3390286a63a038448adcbfb56ded6f73862d6d428e771a5c65ab9a9f611321edb380780a43e1d874fabc3ff1bc299e27a78d89831ab64e2ca52b8acf1173300dd3f0188a07301c85ae9d9f157dbd5f83b74d69934ac63e1d453bdabf7147e6dc52a45d5e76757d65aa7a0b0449ac0fa3d6adb992aaa63e1d450b8acf3143b04db2415c7b6341c8649afd7e90eccd8f936689f857fbe27f3de53b9aff7093200d9380780a43c1e8b4cafd7e911ccd8f13b6bd08526f471ebdd58bae1ed5c2144cb320481a138038048adcbfb56ded3f13768d38526eb71ebd555b9aeed056b12d3310f82e92256910cbfc1f857d8d5ee366ad29934ac63e0d559baaded057412d3390281a6220fdb5aa7c2f35493cebb2c2ec09337ad64e9ca53b8acf1173300d8390e82a5220fc45aa7cafe57dccee26678d8903cae2efd9f42fcbefb143208de2415c7b6341c8649afd7e90eccd8f936689f857fbe27f3de53b9a5f5093500d9380780a43c1e8b4cafd7e911ccd8f13b6bd08526f471ebdd58bae1ed5c2144cb320482a43a038548adcbfb56ded0f3366ed08526eb71ebd555b9aeed056b12d3310f82e92256910cbfc1f854d6d3ec2c2dc09335a962e3c842e0befb1e3b0294244c92e02c17804aa4cae55eded2f03e6ad29835a561e0c842ffbefb163601db2415d8b634148b4ae0d7b0449ac0fa3d69d29a2aa463e1d450b8acf0163a02d82415c7b6341c8649afd7e90eccd8f936689f857fbe27f3de53bbaff7093100d9380780a43a1a8540aecce74499c0fa3f6fd39b28be3bf3de59b0aebc7a2f12996944c4f12c17e825e0d7e915818eb66b0596c66ff93df3de14fae9a45a"
data = decode_xal(extracted_xal)
print(data)  # decoded raw data (always string type)
serialized_data = json.loads(data)
print(serialized_data)  # converted into python object - dictionary
