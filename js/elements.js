// js/elements.js
// 모든 DOM 요소 참조를 한 곳에 모아둡니다. 
// <script type="module">은 defer 속성을 가지므로 문서 로드 후 실행되어 문서 요소에 정상 접근합니다.

// Sliders & value displays
export const currentAgeInput = document.getElementById('current-age');
export const currentAgeVal = document.getElementById('current-age-val');
export const monthlyExpenseInput = document.getElementById('monthly-expense');
export const monthlyExpenseVal = document.getElementById('monthly-expense-val');
export const returnRateInput = document.getElementById('return-rate');
export const returnRateVal = document.getElementById('return-rate-val');
export const inflationRateInput = document.getElementById('inflation-rate');
export const inflationRateVal = document.getElementById('inflation-rate-val');
export const withdrawalRateInput = document.getElementById('withdrawal-rate');
export const withdrawalRateVal = document.getElementById('withdrawal-rate-val');

// Number inputs
export const currentSavingsInput = document.getElementById('current-savings');
export const currentSavingsInputB = document.getElementById('current-savings-b');
export const monthlySavingsInput = document.getElementById('monthly-savings');
export const monthlySavingsInputB = document.getElementById('monthly-savings-b');

// Compare Mode Toggle
export const compareModeToggle = document.getElementById('compare-mode-toggle');
export const compareDashboard = document.getElementById('compare-dashboard');
export const scenarioALabel = document.getElementById('scenario-a-label');
export const planBInputs = document.querySelectorAll('.plan-b-input');
export const labelSavingsA = document.getElementById('label-savings-a');
export const labelReturnA = document.getElementById('label-return-a');
export const labelCurrentA = document.getElementById('label-current-savings-a');
export const labelInflationA = document.getElementById('label-inflation-a');
export const labelSavingsGrowthA = document.getElementById('label-savings-growth-a');

// Additional Slider
export const inflationRateInputB = document.getElementById('inflation-rate-b');
export const inflationRateValB = document.getElementById('inflation-rate-val-b');

// SWR and Savings Growth Elements
export const modeLifeBtn = document.getElementById('mode-life-btn');
export const modeSwrBtn = document.getElementById('mode-swr-btn');
export const lifeExpectancyGroup = document.getElementById('life-expectancy-group');
export const swrRateGroup = document.getElementById('swr-rate-group');
export const swrRateInput = document.getElementById('swr-rate');
export const swrRateVal = document.getElementById('swr-rate-val');

export const savingsGrowthInput = document.getElementById('savings-growth');
export const savingsGrowthVal = document.getElementById('savings-growth-val');
export const savingsGrowthInputB = document.getElementById('savings-growth-b');
export const savingsGrowthValB = document.getElementById('savings-growth-val-b');

// Pension Variables
export const usePensionToggle = document.getElementById('use-pension-toggle');
export const pensionInputs = document.getElementById('pension-inputs');
export const pensionAgeInput = document.getElementById('pension-age');
export const pensionAgeVal = document.getElementById('pension-age-val');
export const pensionAmountInput = document.getElementById('pension-amount');

// Asset Allocation Variables (Plan A)
export const useAssetAllocToggle = document.getElementById('use-asset-alloc-toggle');
export const simpleAssetInput = document.getElementById('simple-asset-input');
export const detailedAssetInput = document.getElementById('detailed-asset-input');
export const returnPlanA = document.getElementById('return-plan-a');
export const assetStockAmount = document.getElementById('asset-stock-amount');
export const assetStockReturn = document.getElementById('asset-stock-return');
export const assetBondAmount = document.getElementById('asset-bond-amount');
export const assetBondReturn = document.getElementById('asset-bond-return');
export const assetRealestateAmount = document.getElementById('asset-realestate-amount');
export const assetTotalDisplay = document.getElementById('asset-total-display');
export const assetReturnDisplay = document.getElementById('asset-return-display');

// Asset Allocation Variables (Plan B)
export const useAssetAllocToggleB = document.getElementById('use-asset-alloc-toggle-b');
export const simpleAssetInputB = document.getElementById('simple-asset-input-b');
export const detailedAssetInputB = document.getElementById('detailed-asset-input-b');
export const returnPlanB = document.getElementById('return-plan-b');
export const assetStockAmountB = document.getElementById('asset-stock-amount-b');
export const assetStockReturnB = document.getElementById('asset-stock-return-b');
export const assetBondAmountB = document.getElementById('asset-bond-amount-b');
export const assetBondReturnB = document.getElementById('asset-bond-return-b');
export const assetRealestateAmountB = document.getElementById('asset-realestate-amount-b');
export const assetTotalDisplayB = document.getElementById('asset-total-display-b');
export const assetReturnDisplayB = document.getElementById('asset-return-display-b');

// Life Events Setup variables
export const addLifeEventBtn = document.getElementById('add-life-event-btn');
export const lifeEventsEditor = document.getElementById('life-events-editor');
export const leDesc = document.getElementById('le-desc');
export const leAge = document.getElementById('le-age');
export const leType = document.getElementById('le-type');
export const leAmount = document.getElementById('le-amount');
export const leSaveBtn = document.getElementById('le-save-btn');
export const leCancelBtn = document.getElementById('le-cancel-btn');
export const lifeEventsList = document.getElementById('life-events-list');

// Calc Mode Elements
export const calcModeAgeBtn = document.getElementById('calc-mode-age-btn');
export const calcModeSavingsBtn = document.getElementById('calc-mode-savings-btn');
export const targetAgeLabel = document.getElementById('target-age-label');
export const targetAgeValContainer = document.getElementById('target-age-val-container');
export const targetAgeInput = document.getElementById('target-age');
export const targetAgeVal = document.getElementById('target-age-val');
export const dualSliderFill = document.getElementById('dual-slider-fill');

export const savingsPlanAGroup = document.getElementById('savings-plan-a-group');
export const savingsPlanBGroup = document.getElementById('savings-plan-b-group');
export const resultLabelA = document.getElementById('result-label-a');
export const resultLabelB = document.getElementById('result-label-b');

// Milestones
export const milestoneContainer = document.getElementById('milestone-container');
export const milestoneList = document.getElementById('milestone-list');

// Results - A
export const targetAssetDisplay = document.getElementById('target-asset-display');
export const retirementAgeDisplay = document.getElementById('retirement-age-display');
export const currentAssetDisplay = document.getElementById('current-asset-display');
export const progressFill = document.getElementById('progress-fill');
export const progressPercentage = document.getElementById('progress-percentage');

// Results - B
export const retirementAgeDisplayB = document.getElementById('retirement-age-display-b');
export const progressFillB = document.getElementById('progress-fill-b');
export const progressPercentageB = document.getElementById('progress-percentage-b');

// Actions / Modals / Buttons
export const themeBtn = document.getElementById('theme-btn');
export const profileModalInvokeBtn = document.getElementById('profile-modal-invoke-btn');
export const chartModalInvokeBtn = document.getElementById('chart-modal-invoke-btn');
export const inflationStressTestBtn = document.getElementById('inflation-stress-test-btn');

export const chartModal = document.getElementById('chart-modal');
export const closeModalBtn = document.getElementById('close-modal-btn');

export const mcModalInvokeBtn = document.getElementById('mc-modal-invoke-btn');
export const mcModal = document.getElementById('mc-modal');
export const closeMcModalBtn = document.getElementById('close-mc-modal-btn');
export const mcLoading = document.getElementById('mc-loading');
export const mcSuccessRate = document.getElementById('mc-success-rate');
export const mcProgressText = document.getElementById('mc-progress-text');

export const profileModal = document.getElementById('profile-modal');
export const closeProfileModalBtn = document.getElementById('close-profile-modal-btn');

export const exportDashboardBtn = document.getElementById('export-dashboard-btn');
export const exportPdfBtn = document.getElementById('export-pdf-btn');

// Other
export const lifeExpectancySelect = document.getElementById('life-expectancy');
export const apiSp500Btn = document.getElementById('api-sp500-btn');
export const apiInflationBtn = document.getElementById('api-inflation-btn');
// Speed Dial
export const speedDial = document.getElementById('speed-dial');
export const speedDialMainBtn = document.getElementById('speed-dial-main-btn');

// Chart Canvases
export const fireChartCtx = document.getElementById('fireChart')?.getContext('2d');
export const mcChartCtx = document.getElementById('mcChart')?.getContext('2d');
