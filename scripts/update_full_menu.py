# -*- coding: utf-8 -*-
"""
Script to update all 37 dishes across 8 categories into order.html
and sync DISH_DETAILS in JavaScript.
"""

new_grid_html = '''            <!-- Two-Column Menu Body (Full 37 Dishes across 8 Categories) -->
            <div class="menu-two-col-grid">
              <!-- CỘT TRÁI: BÁNH CANH GÀ, MÌ GÀ, XÔI, THỨC UỐNG (18 MÓN) -->
              <div class="menu-col-left">
                <!-- Mục 1: BÁNH CANH GÀ. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">BÁNH CANH GÀ.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="bc-xe" data-name="Bánh canh gà xé" data-price="48000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Bánh Canh Gà Xé</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">48K</span>
                        <button class="btn-add-cart" onclick="updateQty('bc-xe', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="bc-xe-trung-non" data-name="Bánh canh gà xé trứng non" data-price="55000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Bánh Canh Gà Xé Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">55K</span>
                        <button class="btn-add-cart" onclick="updateQty('bc-xe-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="bc-dui" data-name="Bánh canh gà đùi" data-price="59000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Bánh Canh Gà Đùi</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">59K</span>
                        <button class="btn-add-cart" onclick="updateQty('bc-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="bc-ma-dui" data-name="Bánh canh má đùi" data-price="68000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Bánh Canh Má Đùi</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">68K</span>
                        <button class="btn-add-cart" onclick="updateQty('bc-ma-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="bc-dac-biet" data-name="Bánh canh gà đặc biệt" data-price="70000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Bánh Canh Gà Đặc Biệt</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">70K</span>
                        <button class="btn-add-cart" onclick="updateQty('bc-dac-biet', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="bc-long-me-trung-non" data-name="Bánh canh lòng mề trứng non" data-price="55000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Bánh Canh Lòng Mề Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">55K</span>
                        <button class="btn-add-cart" onclick="updateQty('bc-long-me-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Mục 2: MÌ GÀ. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">MÌ GÀ.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="mi-xe" data-name="Mì gà xé" data-price="48000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Mì Gà Xé</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">48K</span>
                        <button class="btn-add-cart" onclick="updateQty('mi-xe', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="mi-xe-trung-non" data-name="Mì gà xé trứng non" data-price="55000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Mì Gà Xé Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">55K</span>
                        <button class="btn-add-cart" onclick="updateQty('mi-xe-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="mi-long-me-trung-non" data-name="Mì lòng mề trứng non" data-price="55000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Mì Lòng Mề Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">55K</span>
                        <button class="btn-add-cart" onclick="updateQty('mi-long-me-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="mi-dui" data-name="Mì gà đùi" data-price="59000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Mì Gà Đùi</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">59K</span>
                        <button class="btn-add-cart" onclick="updateQty('mi-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="mi-ma-dui" data-name="Mì gà má đùi" data-price="68000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Mì Gà Má Đùi</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">68K</span>
                        <button class="btn-add-cart" onclick="updateQty('mi-ma-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="mi-dac-biet" data-name="Mì gà đặc biệt" data-price="70000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Mì Gà Đặc Biệt</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">70K</span>
                        <button class="btn-add-cart" onclick="updateQty('mi-dac-biet', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Mục 3: XÔI. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">XÔI.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="xoi-xe-trung-non" data-name="Xôi gà xé trứng non" data-price="40000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Xôi Gà Xé Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">40K</span>
                        <button class="btn-add-cart" onclick="updateQty('xoi-xe-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="xoi-dui-trung-non" data-name="Xôi gà đùi trứng non" data-price="50000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Xôi Gà Đùi Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">50K</span>
                        <button class="btn-add-cart" onclick="updateQty('xoi-dui-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Mục 4: THỨC UỐNG THANH NHIỆT. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">THỨC UỐNG THANH NHIỆT.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="nuoc-nha-dam" data-name="Nha đam mủ trôm" data-price="16000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Nha Đam Mủ Trôm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">16K</span>
                        <button class="btn-add-cart" onclick="updateQty('nuoc-nha-dam', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="nuoc-mu-trom" data-name="Mủ trôm hạt chia" data-price="16000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Mủ Trôm Hạt Chia</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">16K</span>
                        <button class="btn-add-cart" onclick="updateQty('nuoc-mu-trom', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="nuoc-sam" data-name="Sâm rong biển" data-price="16000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Sâm Rong Biển</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">16K</span>
                        <button class="btn-add-cart" onclick="updateQty('nuoc-sam', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="nuoc-pepsi" data-name="Pepsi ướp lạnh" data-price="20000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Pepsi Ướp Lạnh</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">20K</span>
                        <button class="btn-add-cart" onclick="updateQty('nuoc-pepsi', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- CỘT PHẢI: CƠM GÀ, CƠM + GỎI, GỎI, MÓN THÊM (19 MÓN) -->
              <div class="menu-col-right">
                <!-- Mục 5: CƠM GÀ. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">CƠM GÀ.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="com-xe" data-name="Cơm gà xé" data-price="40000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm Gà Xé</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">40K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-xe', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="com-xe-trung-non" data-name="Cơm gà xé trứng non" data-price="47000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm Gà Xé Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">47K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-xe-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="com-dui" data-name="Cơm gà đùi" data-price="52000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm Gà Đùi</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">52K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="com-ma-dui" data-name="Gà má đùi" data-price="65000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Gà Má Đùi</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">65K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-ma-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Mục 6: CƠM + GỎI. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">CƠM + GỎI.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="com-goi-xe" data-name="Cơm gỏi gà xé" data-price="45000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm Gỏi Gà Xé</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">45K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-goi-xe', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="com-goi-xe-trung-non" data-name="Cơm gỏi gà xé trứng non" data-price="52000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm Gỏi Gà Xé Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">52K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-goi-xe-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="com-goi-long-trung-non" data-name="Cơm gỏi lòng gà trứng non" data-price="48000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm Gỏi Lòng Gà Trứng Non</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">48K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-goi-long-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="com-goi-dui" data-name="Cơm gỏi gà đùi" data-price="60000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm Gỏi Gà Đùi</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">60K</span>
                        <button class="btn-add-cart" onclick="updateQty('com-goi-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Mục 7: GỎI. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">GỎI.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="goi-nho" data-name="Gỏi gà ta nhỏ" data-price="50000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Gỏi Gà Ta Nhỏ</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">50K</span>
                        <button class="btn-add-cart" onclick="updateQty('goi-nho', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="goi-lon" data-name="Gỏi gà ta lớn" data-price="100000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Gỏi Gà Ta Lớn</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">100K</span>
                        <button class="btn-add-cart" onclick="updateQty('goi-lon', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="goi-nua-con" data-name="Gỏi gà ta nửa con" data-price="247000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Gỏi Gà Ta Nửa Con</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">247K</span>
                        <button class="btn-add-cart" onclick="updateQty('goi-nua-con', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Mục 8: MÓN THÊM. -->
                <div class="menu-category-block">
                  <div class="menu-category-heading">MÓN THÊM.</div>
                  <div class="compact-dish-list">
                    <div class="compact-dish-item dish-item" data-id="them-com-mi" data-name="Cơm / Mì gói thêm" data-price="5000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cơm / Mì Gói Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">5K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-com-mi', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="them-xoi" data-name="Xôi thêm" data-price="10000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Xôi Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">10K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-xoi', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="them-banh" data-name="Bánh thêm" data-price="10000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Bánh Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">10K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-banh', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="them-ga-xe" data-name="Gà xé thêm" data-price="27000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Gà Xé Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">27K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-ga-xe', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="them-trung-non" data-name="Trứng non thêm" data-price="25000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Trứng Non Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">25K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-trung-non', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="them-co-canh" data-name="Cổ cánh thêm" data-price="30000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Cổ Cánh Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">30K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-co-canh', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="them-long-me" data-name="Lòng mề thêm" data-price="25000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Lòng Mề Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">25K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-long-me', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                    <div class="compact-dish-item dish-item" data-id="them-dui" data-name="Đùi thêm" data-price="35000">
                      <div class="dish-info-left">
                        <span class="compact-dish-name">Đùi Thêm</span>
                      </div>
                      <span class="dish-dots"></span>
                      <div class="dish-action-right">
                        <span class="compact-dish-price">35K</span>
                        <button class="btn-add-cart" onclick="updateQty('them-dui', 1, event)" title="Thêm món">
                          <img src="images/order/add-to-cart.png" alt="Thêm">
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
'''

new_dish_details_js = '''    const DISH_DETAILS = {
      // 1. BÁNH CANH GÀ
      'bc-xe': { title: 'Bánh Canh Gà Xé', price: 48000 },
      'bc-xe-trung-non': { title: 'Bánh Canh Gà Xé Trứng Non', price: 55000 },
      'bc-dui': { title: 'Bánh Canh Gà Đùi', price: 59000 },
      'bc-ma-dui': { title: 'Bánh Canh Gà Má Đùi', price: 68000 },
      'bc-dac-biet': { title: 'Bánh Canh Gà Đặc Biệt', price: 70000 },
      'bc-long-me-trung-non': { title: 'Bánh Canh Lòng Mề Trứng Non', price: 55000 },

      // 2. MÌ GÀ
      'mi-xe': { title: 'Mì Gà Xé', price: 48000 },
      'mi-xe-trung-non': { title: 'Mì Gà Xé Trứng Non', price: 55000 },
      'mi-long-me-trung-non': { title: 'Mì Lòng Mề Trứng Non', price: 55000 },
      'mi-dui': { title: 'Mì Gà Đùi', price: 59000 },
      'mi-ma-dui': { title: 'Mì Gà Má Đùi', price: 68000 },
      'mi-dac-biet': { title: 'Mì Gà Đặc Biệt', price: 70000 },

      // 3. XÔI
      'xoi-xe-trung-non': { title: 'Xôi Gà Xé Trứng Non', price: 40000 },
      'xoi-dui-trung-non': { title: 'Xôi Gà Đùi Trứng Non', price: 50000 },

      // 4. THỨC UỐNG THANH NHIỆT
      'nuoc-nha-dam': { title: 'Nha Đam Mủ Trôm', price: 16000 },
      'nuoc-mu-trom': { title: 'Mủ Trôm Hạt Chia', price: 16000 },
      'nuoc-sam': { title: 'Sâm Rong Biển', price: 16000 },
      'nuoc-pepsi': { title: 'Pepsi Ướp Lạnh', price: 20000 },

      // 5. CƠM GÀ
      'com-xe': { title: 'Cơm Gà Xé', price: 40000 },
      'com-xe-trung-non': { title: 'Cơm Gà Xé Trứng Non', price: 47000 },
      'com-dui': { title: 'Cơm Gà Đùi', price: 52000 },
      'com-ma-dui': { title: 'Gà Má Đùi', price: 65000 },

      // 6. CƠM + GỎI
      'com-goi-xe': { title: 'Cơm Gỏi Gà Xé', price: 45000 },
      'com-goi-xe-trung-non': { title: 'Cơm Gỏi Gà Xé Trứng Non', price: 52000 },
      'com-goi-long-trung-non': { title: 'Cơm Gỏi Lòng Gà Trứng Non', price: 48000 },
      'com-goi-dui': { title: 'Cơm Gỏi Gà Đùi', price: 60000 },

      // 7. GỎI
      'goi-nho': { title: 'Gỏi Gà Ta Nhỏ', price: 50000 },
      'goi-lon': { title: 'Gỏi Gà Ta Lớn', price: 100000 },
      'goi-nua-con': { title: 'Gỏi Gà Ta Nửa Con', price: 247000 },

      // 8. MÓN THÊM
      'them-com-mi': { title: 'Cơm / Mì Gói Thêm', price: 5000 },
      'them-xoi': { title: 'Xôi Thêm', price: 10000 },
      'them-banh': { title: 'Bánh Thêm', price: 10000 },
      'them-ga-xe': { title: 'Gà Xé Thêm', price: 27000 },
      'them-trung-non': { title: 'Trứng Non Thêm', price: 25000 },
      'them-co-canh': { title: 'Cổ Cánh Thêm', price: 30000 },
      'them-long-me': { title: 'Lòng Mề Thêm', price: 25000 },
      'them-dui': { title: 'Đùi Thêm', price: 35000 }
    };'''

with open('order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace HTML .menu-two-col-grid
start_marker = '<div class="menu-two-col-grid">'
end_marker = '<!-- Footer: address & contact -->'

idx1 = content.find(start_marker)
idx2 = content.find(end_marker)

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + new_grid_html.strip() + '\n\n            ' + content[idx2:]
    print('HTML grid replaced successfully!')
else:
    print('Could not find HTML grid markers! idx1:', idx1, 'idx2:', idx2)

# Replace JS DISH_DETAILS
js_start_marker = 'const DISH_DETAILS = {'
js_end_marker = '};\n\n    // Khởi tạo DOM'
if js_end_marker not in content:
    js_end_marker = '};\r\n\r\n    // Khởi tạo DOM'

idx_js1 = content.find(js_start_marker)
idx_js2 = content.find(js_end_marker)

if idx_js1 != -1 and idx_js2 != -1:
    content = content[:idx_js1] + new_dish_details_js.strip() + '\n' + content[idx_js2 + 2:]
    print('JS DISH_DETAILS replaced successfully!')
else:
    print('Could not find JS DISH_DETAILS markers! idx_js1:', idx_js1, 'idx_js2:', idx_js2)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done updating order.html!')
